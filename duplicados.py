import os

print("""Con este sencillo script se eliminarán aquellos archivos duplicados de dos carpetas diferentes(aunque tengan distintos nombres
        PASOS:
        1 - Primero copia la ruta de la carpeta donde haya archivos duplicados que quieras borrar.
        2 - Después pega la ruta de la otra carpeta donde contenga los otros archivos duplicados (estos archivos no se borrarán)""")


rutaorigen = input("Escribe la ruta de la carpeta que tenga archivos duplicados que quieras borrar: ")
rutadestino = input("Escribe la ruta de la otra carpeta que tenga archivos duplicados (los archivos de esta carpeta no se eliminarán: ")



archivosrutaorigen = os.listdir(rutaorigen)
archivosrutadestino = os.listdir(rutadestino)

 
for i in archivosrutaorigen:
    os.chdir(rutaorigen)
    size = os.stat(i).st_size
    for a in archivosrutadestino:
        os.chdir(rutadestino)
        size2 = os.stat(a).st_size
        if size == size2:
            os.chdir(rutaorigen)
            os.remove(i)



