# codeTranslator
Pablo Contreras
201973572-1

Traducto de codigos y bases para Arquitectura de Sistemas 2021.

Aclaraciones:
    
    - Los códigos gray transforman de indices binarios a el numero decimal que estos    deberian representar, y de este número a cualquier base que se necesite. No sigue el ejemplo de la tarea, porque a mi parecer, está erróneamente explicado.

    - Si bien la tarea pide un solo archivo .py con el código fuente, me parece que por el bien del orden y de las buenas prácticas, es necesario modularizar, espero se tenga en cuenta esto y no se me aplique un descuento. 

    - El código se divide un una función main y un paquete, donde están definidas funciones en los archivos codeBase.py y decimalBase.py, y modelos de algunas variables en models.py . 

    - codeBase.py implica en su mayoría funciones relacionadas a la conversión de códigos  y bases.
    
    - decimalBase.py implica en su mayoría funciones relacionadas a la conversión de decimales y códigos. 

    - models.py guarda variables usadas a lo largo del programa.

    - main.py ejecuta la función main, donde se loopea y piden los inputs necesarios, la capa que procesa la data es decimalBase.py, allí encontrarás la función resolveBases, quien hace la asignación de las variables a sus funciones pertinentes y resuelve la conversión.

    - Pylint me señala muchos errores y warnings respecto a los imports, creo que es por un tema de que se deprecó el uso de __all__ en los exports. No debería afectar la ejecución en ningún caso, y si no utilizas pylint como verificador entonces puedes ignorar esta aclaración.

    - Siguiendo con el problema de Pylint, advierto que puede dar comportamientos indeterminados el ejecutar el código desde VisualStudio Code con la extensión de Python desde la interfaz, por lo tanto, ejectuar el código desde la consola de preferencia llamando al interprete de Python.

Repositorio por si acaso:
    https://github.com/MenitoX/codeTranslator