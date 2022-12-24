import zipfile

#Descomprimir archivos zip
archivo_zip = zipfile.ZipFile('C:\\users\\pc\\Documents\documentos.zip')
archivo_zip.extractall('C:\\users\\pc\\Documents\\ficheros_descomprimidos\\documentos_extraidos')

print("Descomprimiendo:")
print(archivo_zip.namelist())

archivo_zip.close()
