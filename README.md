# Topicos Especiales En Telematica - Proyecto 2 HPC

## Creado por: Maria Clara Sanchez V, Tomas Alvarez G y Juan Esteban Fonseca P.

#### Para este proyecto se realizó un algoritmo de analitica de texto, el cual consiste en un wordcount en diferentes Datasets (.csv), donde por cada palabra que se ingrese por teclado, se liste en orden descendente por frecuencia de palabra en el contenido de la noticia, las noticias más relevantes.

#### El formato de busqueda debe ser asi: max 10, frecuencia de la palabra de la noticia, identificacion de la noticia, titulo de la noticia. La palabra debe ser ingresada por el usuario vis command prompt.

#### Se tiene tambien una forma de implemetacion serial (la cual se encuentra en la carpeta serial) y la forma de implementacion en paralelo con OpenMP (en la carpeta OpenMP) y MPI (en la carpeta MPI)

## Forma de compilacion

### Serial
#### Para compilar el algoritmo serial se necesita tener python3 y se hace dentro de la carpeta serial asi: 
    $ python T2.py

### MPI 
#### Para compilar el algoritmo MPI se necesita tener python3 y mpi4py, se hace dentro de la carpeta MPI asi: 
    $ mpiexec -f ../hosts_mpi -n <numero de cores deseados> /opt/anaconda3/bin/python test1.py
    
### OpenMP
#### Para compilar el algoritmo OpenMP se necesita tener el compilador de c++ en una version igual o mayor a la 4.9, se hace dentro de la carpeta OpenMP asi:
    $ g++ -std=c++11 wordCount.cpp -o wordCount -fopenmp
    
#### y para ejecutarlo
    $ export OMP_NUM_THREADS=<numero deseado de hilos>
    $ export OMP_DISPLAY_ENV='true'
    $ ./wordCount
  
