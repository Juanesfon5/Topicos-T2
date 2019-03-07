#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

static int numeroPalabras(string texto, string palabra){
    stringstream input(texto);
    int cnt=0;
    while(input>>texto)
    {
        if(texto == palabra)
          cnt++;
    }
    return cnt;
}

static void contar(string archivo, vector<vector<string>> csv){
    string linea;
    string palabra = "";
    int cantidadPalabra = 0;
    int count = 1;
    vector<string> input;
    vector<string> id;
    vector<string> title;
    vector<string> content;
    vector<int> contador;
    ifstream archivoPy(archivo);
    while(getline(archivoPy, linea,'\\')){
        input.push_back(linea);
    }
    cout << input.size() << endl;
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
    //transform (palabra.begin(), palabra.end(), palabra.begin(), ::tolower);
    for(int i=0;i<content.size();i++){
      //transform (content.at(i).begin(), content.at(i).end(), content.at(i).begin(), ::tolower);
      //transform (title.at(i).begin(), title.at(i).end(), title.at(i).begin(), ::tolower);
        cantidadPalabra = numeroPalabras(content.at(i), palabra) + numeroPalabras(title.at(i), palabra);
        contador.push_back(cantidadPalabra);
    }
    for(int i=0;i<contador.size();i++){
      cout << contador.at(i) << "/ " << id.at(i) << "/ " << title.at(i) << endl;
      //cout << id.at(i) << endl;
    }


}

int main(int argc, char* argv[]) {
  string archivo = "output.txt";
  vector<vector<string>> output;
  contar(archivo, output);
  return 0;
}
