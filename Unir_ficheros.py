from PyPDF2 import PdfFileMerger, PdfFileWriter
import os
import msvcrt
print("*** Union de ficheros PDF para Tabarato, SA de CV ***")
print("por JEMD GitHub: emena16 v1.1")
print("*Recuerde descomprimir o pegar los ficheros a unir en la carpeta: Ficheros_A_Unir")
print("")


print("Presione espacio ' ' para continuar...")
key = None
while key != ' ':
    key = msvcrt.getwch()
#Buscamos los ficheros que vamos aunir que tengan el formato PDF
pdfs = [archivo for archivo in os.listdir('Ficheros_A_Unir/') if archivo.endswith(".pdf")]
print("Se han encontrado: "+repr(len(pdfs))+" ficheros a unir.")
print("")

if len(pdfs)<1:
    print("Error! No se encontraron PDF a unir, por favor pegue los fiechos a unir en")
    print("la carpeta Ficheros_A_Unir para que podamos trabajar.")

nombre_archivo_salida = repr(len(pdfs))+" ficheros_unidos.pdf"
#Creamos el objeto fucionador que se encargara de gestionar los ficheros
fusionador = PdfFileMerger()
#Comenzamos a unir recorriendo fichero por fichero y los vamos uniendo 1 con el siguiente hasta terminar
for pdf in pdfs:
    print('Uniendo: '+pdf)
    fusionador.append(open('Ficheros_A_Unir/'+pdf, 'rb'))

#Escribimo todo a un nuevo fichero de salida para poder verlo
with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)

print()
print("Se han unido: "+repr(len(pdfs))+" ficheros PDF")
