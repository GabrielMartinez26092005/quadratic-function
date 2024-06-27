# quadratic-function
*DESCRIPCION: Este proyecto tiene la finalidad de resolver una ecuacion cuadratica de segundo grado mediante el lenguaje python. 

*USO: Para utilizar correctamente este codigo, hay que seguir los siguientes pasos:
    *PRIMERO: Crear una instancia de la clase FuncionCuadratica().
    *SEGUNDO: Llamar al metodo ingreso_dato() y pasarle por parametros los respectivos coeficientes a, b y c.
    *TERCERO: Llamar al metodo calcular_discriminante().
    *CUARTO: Llamar al metodo evaluar_discriminante().
    *QUINTO: LLamar al metodo mostrar_resultado().

*EXPLICACION: Aqui una explicacion de cada paso mas a detalle:
    *PRIMERO: En este paso se crea una instancia de la clase FuncionCuadratica() para luego poder trabajar con sus metodos.
    *SEGUNDO: Al llamar al metodo ingreso_dato(), se pide al usuario los valores de los 3 coeficientes guardandolos en una lista (el coeficiente a no puede ser igual a 0).
    *TERCERO: Al llamar al metodo calcular_discriminante(), se calcula el valor de la discriminante y la guarda en una variable.
    *CUARTO: El metodo evaluar_discrimimante() se utiliza el discriminante para saber cuantas soluciones tiene la funcion, y dependiendo de cuantas soluciones hay, eligira un camino u otro para resolver la ecuacion. Finalmente guarda el o los valores de la funcion en la lista valores_calculados.
    *QUINTO: En el ultimo metodo mostrar_resultados(), se muestran los resultados obtenidos, dependiendo cuantos elementos (resultados) tiene la lista valores_calculados. 
