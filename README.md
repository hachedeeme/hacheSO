Trabajo final para la materia Sistemas Operativos de la UNQ
=======
Profesores: Federico Repond, Marcelo Tondato

# Que se implementó?
Un programa que simula la funcionalidad de un sistema operativo, implementando diferentes comportamientos para cada uno de sus componentes para entender mejor cómo estos funcionan con diferentes configuraciones.

**Kernel:** Principalmente el kernel, es el que engloba todos los componentes y los usa de manera tal que se puede simular que hay varios programas corriendo de manera simultánea.

**Instruction:** Se implementaron varios tipos de instrucciones,  se dividen entre instrucciones de CPU y de I/O.

**Program:** Los programas, que estan formados por instrucciones, son los componentes que el Kernel puede ejecutar, sus instrucciones serán cargadas en memoria y se creará un proceso que pronto será ejecutado.

**Pcb:** Es la abstracción de proceso, posee varias características que lo ayudan pasar por diferentes instancias de ejecución hasta ser terminado.

**PcbState:** Representan los estados que un Pcb puede tener a lo largo de su vida, entre ellos estan: NEW, READY, RUNNING, IO y FINISH.

##Hardware
**HardDisk:** Representa el disco duro, es un componente de almacenamiento para los programas, los programas se buscan en disco previo a cargarlos en memoria.

**Memory:** La memoria es donde las instrucciones de los diferentes programas que se estan ejecutando se van a cargar, la Cpu va a tener que acceder a memoria para obtener la instrucción actual a ejecutar. Cuando un programa termina su ejecución el espacio de la memoria que este ocupaba es liberado.

**Cpu:** Es el encargado de ejecutar las instrucciones de cpu. Luego de que un proceso termine sus correspondientes rafagas de ejecución puede o bien terminar el proceso y liberarlo, devolverlo a la cola de ready o mandarlo a hacer entrada salida si la instrucción actual de ese proceso es de entrada salida.
IODevice: Es el componente que se encarga de ejecutar las instrucciones de entrada salida, luego de ejecutar, el proceso puede terminar o volver a la cola de ready.

**Clock:** El Clock es un componente que ayuda a ejecutar en simultáneo varios objetos, actualmente se utiliza para la Cpu, el IODevice y el InterruptionManager que se va a hablar de él más adelante.

## Scheduling
**LongTermScheduler:** Es el planificador de largo plazo, su función es elegir los nuevos procesos que se van creando y ponerlos en la cola de ready para que puedan ser seleccionados para ser ejecutados. También se encarga de terminar los procesos que ya terminaron su ejecución.

**ShortTermScheduler:** Es el planificador de corto plazo, se encarga de elegir el proceso de la cola de ready para que la cpu los ejecute. Este trabaja con varias políticas diferentes:
 - **Fifo:** Primero que entra, primero que sale. Esta política solo da una rafaga de cpu a un proceso para que se ejecute. Siempre agarra el primero.
 - **RoundRobin:** Funciona como Fifo, siempre agarra el primero, pero la diferencia es que se le puede definir un número mayor de rafagas de cpu que un proceso puede estar en cpu. Este valor se denomina quantum.

## Interruption management
**Interruption:** Las interrupciones son los objetos que determinan cuál es el siguiente paso de un proceso en determinado momento. Se pueden mencionar las siguientes:
 - **NewPcb:** Que se da cuando se crea un nuevo proceso, se pone el nuevo proceso en la cola de ready y se le setea el estado “READY”.
 - **TimeOut:** Cuando se le acaban las rafagas de cpu a un proceso y este todavía tiene instrucciones para ejecutar, se tira la interrupción de TimeOut que hace que el proceso vuelva a la cola de ready para que compita por cpu nuevamente.
 - **FinishPcb:** Cuando un proceso termina su ejecución, se lanza esta interrupción para que luego se mate el proceso y se libere la memoria.
 - **IOInterruption:** Es cuando la Cpu está corriendo un proceso y se topa con que la instrucción actual a ejecutar es de entrada salida, se arroja esta interrupción para que el IODevice pueda correr ese proceso.

**InterruptionManager:** Este componente está a la espera de nuevas interrupciones, cuando una o varias de estas llegan, el InterruptionManager se encarga de manejarlas todas, causando el impacto que tenga que causar en el sistema, para luego ponerse nuevamente a la espera de mas interrupciones.

## Memory management
**MemoryManagementUnit:** MMU en adelante, es el componente que se encarga de interactuar con la memoria, cargar programas, liberar el espacio que ocupaba un proceso a la memoria, hacer el fetch de instrucción, entre otras cosas. Hay dos tipos de MMU:

**ContinousAllocation:** Consiste en la asignación de bloques para cada proceso, lleva la cuenta de los bloques libres y los bloques que ya fueron asignados a los procesos. Cada vez que se tiene que cargar un nuevo proceso en memoria, el MMU de asignación continua tiene que asignarle un bloque vacío que sea de tamaño suficiente para alojarlo, para esto la asignación continua emplea tres tipos de algoritmos:
 - **FirstFit:** Devuelve el primer bloque que satisface al proceso.
 - **BestFit:** Devuelve el primero de menor tamaño suficiente que satisface al proceso. Para esto el BestFit mantiene el orden de los bloques de menor a mayor tamaño y devueleve el primero que encuentra del tamaño adecuado.
 - **WorstFit:** Devuelve el bloque de tamaño más grande. Para esto el WorstFit mantiene el orden de los bloques vacíos de mayor a menor tamaño y siempre devuelve el primero.
Si al cargar un proceso a memoria no se encuentra un bloque que safisfaga al nuevo proceso, la asignación continua emplea un algoritmo compactación para generar nuevos bloques de mayor tamaño.

=================================================================

Hago un espacio especial en el informe para explicar un poco cómo fue que resolví el tema de la Paginación en el trabajo, que era lo último que me faltaba hacer:

Como el trabajo no está acoplado a una sola forma de manejo de memoria, pude cambiar la configuración del Kernel fácilmente para que use la nueva MMU implementada, osea Paginación, ahora se puede usar tanto paginación como asignación continua. 
A continuación voy a explicar brevemente y a grandes rasgos cómo funciona mi estrategia de Paginación diciendo cómo se crea y cómo funciona su interfaz:

Una MMU **Paging** se crea con la memoria que va a manejar y un tamaño de página para definir las páginas en las que se va a “dividir” la memoria, también tiene una tabla de páginas (**PageTable**) que es la que divide la memoria en marcos y lleva la cuenta de los procesos que estan en memoria con sus respectivas páginas donde fueron asignados por la MMU de paginación. 
En el momento de hacer un fetch de instrucción, la **Paging** con la ayuda de la tabla de páginas traducen la direccion logica pedida por la direccion física correspondiente para devolver la instrucción actual desde memoria.
Cuando se carga un programa, se pide una cantidad determinada de páginas que depende de cuantas instrucciones tenga el programa que se está cargando y del tamaño de página definido, la tabla de páginas registra el futuro proceso con sus respectivas páginas asignadas y luego el programa es cargado en memoria según las páginas que se le asignaron.
Cuando se quiere liberar un proceso de la memoria, se obtiene las páginas asignadas a ese proceso y luego se va borrando la información que tiene la memoria de cada una de las páginas, luego las páginas que fueron desasignadas se tienen nuevamente en cuenta para los procesos que se corran en el futuro.