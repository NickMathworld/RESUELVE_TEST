# RESUELVE_TEST
Proyecto en python para resolver la problemática de los sueldos de los jugadores de la liga de RESUELVE
## CÓMO EJECUTAR EL PROYECTO
Para ejecutar el proyecto necesitaremos lo siguiente
* Python3+
* Una terminal abierta
#### 
Abrimos la terminal y nos ubicamos en la carpeta del proyecto. 
#### 
Para ejecutarlo simplemente en la terminal corremos el comando python3 
###
      python3 test.py
#### En el que nos puede regresar 3 posibles resultados
* OK: SE CALCULARON LOS SUELDOS SIN NINGÚN PROBLEMA
* ERROR AL ABRIR ARCHIVO JSON: NO SE ENCUENTRA EL ARCHIVO O HUBO ALGUN INCONVENIENTE AL ABRIR EL ARCHIVO JSON
* ERROR AL VALIDAR JSON: LOS DATOS QUE VENÍAN EN EL ARCHIVO JSON NO TENÍAN EL FORMATO ADECUADO
#### 
En el caso de que nos mande el mensaje de OK se creará un archivo llamado "data_test_out" en el que se desplegará el JSON ya con la información completa
### CÓMO CREAR CASOS DE PRUEBA
Abrimos el archivo data_test, en el que ahí pegaremos el caso de prueba para que lo ejecute el sistema
###
      [  
         {  
            "nombre":"Juan Perez",
            "nivel":"C",
            "goles":10,
            "sueldo":50000,
            "bono":25000,
            "sueldo_completo":null,
            "equipo":"rojo"
         },
         {  
            "nombre":"EL Cuauh",
            "nivel":"Cuauh",
            "goles":30,
            "sueldo":100000,
            "bono":30000,
            "sueldo_completo":null,
            "equipo":"azul"
         },
         {  
            "nombre":"Cosme Fulanito",
            "nivel":"A",
            "goles":7,
            "sueldo":20000,
            "bono":10000,
            "sueldo_completo":null,
            "equipo":"azul"

         },
         {  
            "nombre":"El Rulo",
            "nivel":"B",
            "goles":9,
            "sueldo":30000,
            "bono":15000,
            "sueldo_completo":null,
            "equipo":"rojo"

         }
      ]
#### El sistema valida los valores del JSON, por lo que para que sea válido debe cumplir que:
* nivel: Solo puede ser A B C o Cuauh, en cualquier otro caso será inválido el archivo JSON,
* goles: Debe  ser tipo numérico,
* sueldo: Debe ser tipo numérico,
* bono: Debe ser tipo numérico,
#### Para ejecutar las pruebas unitarias se debe de ejecutar con el siguiente comando
      python -m doctest -v test.py
####
Dando como resultado
####
      Trying:
          calcula_sueldos("data_in")
      Expecting:
          'OK'
      ok
      Trying:
          calcula_sueldos("data_error")
      Expecting:
          'ERROR AL VALIDAR JSON'
      ok
      Trying:
          calcula_sueldos("data_error_noexiste")
      Expecting:
          'ERROR AL ABRIR ARCHIVO JSON'
      ok
      2 items had no tests:
          test
          test.crea_jugador
      1 items passed all tests:
         3 tests in test.calcula_sueldos
      3 tests in 3 items.
      3 passed and 0 failed.
      Test passed.
