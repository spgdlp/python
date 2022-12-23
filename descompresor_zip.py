import zipfile

#Descomprimir archivos zip
archivo_zip = zipfile.ZipFile('D:\\ficheros_comprimidos\\documentos.zip')
archivo_zip.extractall('D:\\ficheros_descomprimidos\\')

print("Descomprimiendo:")
print(archivo_zip.namelist())

archivo_zip.close()