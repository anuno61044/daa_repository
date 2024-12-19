# Definición del problema

Una empresa encargada de hacer desarrollo de software, quiere ver como repartir tareas a sus trabajadores. Cada tarea tiene un tiempo estimado de ralización, una ganancia y una fecha límite para entregarse. Los trabajadores tienen un salario por tarea que puede ser distinto para cada trabajador y una experiencia que influye en el tiempo que demoran en resolver la tarea. Además solo pueden resolver una tarea a la vez.

El objetivo es buscar la mejor forma de asignar las tareas de modo que se obtenga la ganancia máxima y se realicen todas la tareas. Si no es posible realizar todas las tareas, entonces la mayor cantidad.

## Importanciad del problema

Resolver este problema permite maximizar las ganancias totales de la empresa. Asiganar las tareas de una mejor manera, garantizando que se cumpla la mayor cantidad posible y dentro del tiempo establecido, lo que permite ganar y mantener la reputación del cualquier empresa. Además brinda un mejor uso de los recursos humanos, evitando la sobrecarga de algunos trabajdores y el subuso de otros.

### Complejidad

Este problema es un caso de optimización combinatoria y, en general, es NP-hard.
Los factores que contribuyen a la complejidad son:

• Número de variables: El número de posibles asignaciones de tareas a trabajadores crece exponencialmente con el número de tareas y trabajadores. Cada tarea puede asignarse a varios trabajadores, añadiendo más complejidad.

• Restricciones: Las restricciones (fechas límite, experiencia requerida, salarios variables) hacen que el espacio de búsqueda de soluciones sea más complejo de explorar.
