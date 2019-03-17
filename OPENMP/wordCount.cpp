#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <omp.h>
#include <omp.h>
#include <map>
#include <regex>

using namespace std;

static int numeroPalabras(string texto, string palabra){
  int cnt=0;
  regex rgx("\\w+");
  regex_iterator<string::iterator> it(texto.begin(), texto.end(), rgx);
  regex_iterator<string::iterator> end;
  for(; it != end; ++it){
    if((it->str()) == palabra){
      cnt++;
    }
  }
  return cnt;
}

static void contar(string archivo, vector<vector<string>> csv){
  string linea;
  string palabra = "";
  map<int, int> auxiliar;
  int count = 1;
  vector<string> input;
  vector<string> id;
  vector<string> title;
  vector<string> content;
  vector<int> copia,copia2;
  ifstream archivoPy(archivo);
  while(getline(archivoPy, linea,'\'')){
    input.push_back(linea);
  }
  for(int i=0;i<input.size();i++){
    if(count == 1){
      id.push_back(input.at(i));
    }
    else if(count == 2){
      title.push_back(input.at(i));
    }
    else if(count == 3){
      content.push_back(input.at(i));
    }
    count++;
    if(count > 3){
      count = 1;
    }
  }
  cout << "Ingrese la palabra que desee buscar:";
  getline(cin, palabra);
  transform (palabra.begin(), palabra.end(), palabra.begin(), ::tolower);
  
#pragma omp parallel
  {
    vector<int> contador;
    int cantidadPalabra = 0;
#pragma omp for schedule(static)
    for(int i=0;i<content.size();i++){
      transform (content.at(i).begin(), content.at(i).end(), content.at(i).begin(), ::tolower);
      transform (title.at(i).begin(), title.at(i).end(), title.at(i).begin(), ::tolower);
      cantidadPalabra = numeroPalabras(content.at(i), palabra) + numeroPalabras(title.at(i), palabra);
      auxiliar[i] = cantidadPalabra;
      contador.push_back(cantidadPalabra);
    }
#pragma omp critical
    {
      copia.insert(copia.end(), make_move_iterator(contador.begin()), make_move_iterator(contador.end()));
    }     
  }
  cout << auxiliar.size() << endl;
  copia2=copia;
  sort(copia.begin(),copia.end());
  reverse(copia.begin(),copia.end());
  int i = 0;
  while(i<=9){
    for(int j=0;j<auxiliar.size();j++){
      if((auxiliar.at(j) == copia.at(i))  && (i <= 9)){
	cout << copia.at(i) << "/ " << id.at(j) << "/ " << title.at(j) << endl;
	i++;
      }
    }
  }
}

int main(int argc, char* argv[]) {
  string command = "python readcsv.py";
  system(command.c_str());
  string archivo = "output.txt";
  vector<vector<string>> output;
  contar(archivo, output);
  return 0;
}
