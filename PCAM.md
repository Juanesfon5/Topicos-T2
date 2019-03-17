### Al principio del proyecto decidimos utilizar python para el algoritmo serial ya que en este teníamos muchas facilidades a la hora de leer directorios y los archivos, y también métodos que ayudaban a la solución del problema (contar palabras)

### Partitioning: 
#### El algoritmo consiste de varias partes. Inicialmente, se recorre el directorio de los datasets y se lee cada archivo .csv. Con cada archivo en un diccionario de python, se filtraba solo el título,el ID y el contenido de cada uno y se realizaba el conteo de la palabra que anteriormente se le pasa al usuario dentro de cada archivo. 

#### El conteo se realiza utilizando una función de python que recibe una expresión regular y pasa a una lista todo lo que cumpla con dicha expresión regular. En nuestro caso, utilizamos una expresión regular que solo recibe caracteres de letras de la ‘a’ a la ‘z’, filtrando así los caracteres especiales o signos de puntuación. 

#### Con la lista hecha, se utiliza la función de count() para listas de python, el cual busca cuantas veces encuentra la palabra indicada en la lista, sin contar las palabras compuestas (Por ejemplo, si la palabra ingresada es “House”, la función no contará la palabra “firehouse”).

#### Después de realizar el conteo, si en la noticia se encontró más de una repetición de la palabra ingresada, se agrega el título de la noticia, su identificación y el conteo de la palabra a una nueva lista. Esta, al final del conteo de todas las noticias, se organiza según los conteos de la palabra en cada noticia de forma descendente y se toman e imprimen las 10 primeras posiciones, las cuales representan las 10 noticias con un mayor número de repeticiones de la palabra ingresada en cada noticia.

### Communication: 
#### En OpenMP la comunicación entre tareas no se hace explícita ya que es memoria compartida, lo que hace que cada hilo pueda escribir en la misma posición de memoria al mismo tiempo, por eso se puede producir la condición de carrera; Ya que en nuestro código tenemos un arreglo que contiene los diferentes títulos y un arreglo que contiene los diferentes contenidos de cada noticia, al hacerse la paralelización, los hilos se reparten ambos arreglos de forma automática, y ejecutan el algoritmo con su parte del arreglo. Para evitar una posible condición de carrera en nuestro código se decidió poner una sección crítica a la hora de juntar el resultado del algoritmo con cada arreglo en un arreglo maestro.

#### En MPI por otra parte, es memoria distribuida, por lo tanto cada procesador tiene una copia de cada objeto instanciado dentro de la paralelización, por lo tanto nunca habrá condición de carrera. Para nuestro código decidimos usar el método Broadcast, Gather y Scatter para la comunicación entre cores; Broadcast para que cada core tuviera una instancia de la palabra ingresada, Scatter para repartir uniformemente el arreglo del contenido de las noticias y sus títulos y al final un Gather para recolectar organizadamente los resultados de la tarea con cada pedazo de los arreglos.

### Agglomerated: 
#### Al analizar la problemática, en ambos códigos de la solución (MPI y OpenMP)  se dividió en pequeñas tareas simples. No se vió una necesidad de aglomerar tareas en tareas más grandes

### Mapping: 
#### Para OpenMP la división de tareas se hace “automática” dentro del programa ya que solo hay que decir que se va a paralelizar por medio de la instrucción #pragma omp parallel, con esta instrucción se dice desde qué parte se paraleliza, para luego usar #pragma omp for lo que indica que se va a paralelizar el ciclo for, al hacer esto lo que se realizará es que la información se repartirá de acuerdo al número de hilos con el que se le haya puesto a ejecutar, y la información que se repartirá es la que se va a “procesar” dentro del ciclo, que en nuestro caso sería el conteo de palabras dentro del contenido de las  noticias y los títulos de las mismas.

#### En MPI para repartir el trabajo lo hacíamos por medio del nodo “master” el cual tenía el identificador cero, este nodo se encargaba de repartir los arreglos previamente partidos a partir del arreglo “maestro”, luego de hacer la repartición del arreglo se pasa al procesamiento de estos y cuando todos hayan acabado se pasará a hacer un gatter, el cual reunirá toda la información en el master y luego terminar el “procesamiento” que es solo el ordenamiento del arreglo del conteo para sacar los 10 primeros.
