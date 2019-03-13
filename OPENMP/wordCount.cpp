#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <omp.h>
#include <omp.h>
#include <map>

using namespace std;

static int numeroPalabras(string texto, string palabra){
    stringstream input(texto);
    int cnt=0;
    while(input>>texto)
    {
      if((texto == palabra) || (texto == palabra+',') || (texto == palabra+'.') || (texto == palabra+'!') || (texto == palabra+'?') ||
	 (texto == palabra+';') || (texto == palabra+':'))
          cnt++;
    }
    return cnt;
}

static void contar(string archivo, vector<vector<string>> csv){
    string linea;
    string palabra = "";
    //int cantidadPalabra = 0;
    map<int, int> auxiliar;
    int count = 1;
    vector<string> input;
    vector<string> id;
    vector<string> title;
    vector<string> content;
    // vector<int> contador;
    vector<int> copia,copia2;
    ifstream archivoPy(archivo);
    while(getline(archivoPy, linea,'\'')){
        input.push_back(linea);
    }
    //cout << input.size() << endl;
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
      //cout << contador.size() << endl;
      //}
      //cout << contador.size() << endl;
#pragma omp critical
{
      //copia = contador;
      copia.insert(copia.end(), make_move_iterator(contador.begin()), make_move_iterator(contador.end()));
}     //cout << copia.size() << "Holi no joda" << copia.at(0)  << endl;
     
      //cout << copia.size() << endl;
      /*
      sort(contador.begin(), contador.end());
      reverse(contador.begin(), contador.end());
      cout << contador.at(0) << " " << copia.at(0) << endl;
      */
  
      /*int i = 0;
      while(i<=9){
	for(int j=0;j<copia.size();j++){
	  if((contador.at(i)==copia.at(j)) && (i <= 9)){
	    cout << contador.at(i) << "/ " << id.at(j) << "/ " << title.at(j) << endl;
	    i++;
	  }
	}
	}*/

    }
    cout << auxiliar.size() << endl;
    copia2=copia;
    sort(copia.begin(),copia.end());
    reverse(copia.begin(),copia.end());
    //cout << copia.at(0) << endl;
    /*int i = 0;
    while(i<=9){
      for(int j=0;j<copia2.size();j++){
	if((copia.at(i)==copia2.at(j)) && (i <= 9)){
	  cout << copia.at(i) << "/ " << id.at(j) << "/ " << title.at(j) << endl;
	  i++;
	}
      }
      }*/
    int i = 0;
    while(i<=9){
      for(int j=0;j<auxiliar.size();j++){
	if(auxiliar.at(j) == copia.at(i)){
	  cout << copia.at(i) << "/ " << id.at(j) << "/ " << title.at(j) << endl;
          i++;
	}
      }
    }
    // cout << copia.size();
}

int main(int argc, char* argv[]) {
  string command = "python readcsv.py";
  system(command.c_str());
  string archivo = "output.txt";
  vector<vector<string>> output;
  contar(archivo, output);
  return 0;
}
