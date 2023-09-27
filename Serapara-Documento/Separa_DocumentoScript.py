import PyPDF2

def split_pdf(input_pdf_path, output_folder):
    # Abre el archivo PDF de entrada
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        # Recorre todas las páginas del PDF
        for page_num in range(pdf_reader.numPages):
            # Crea un nuevo PDF con una sola página
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page_num))
            
            # Define el nombre del archivo de salida
            output_pdf_path = f"{output_folder}/{page_num + 1}.pdf"
            
            # Guarda la página en el archivo de salida
            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)
                
            print(f"Se ha creado {output_pdf_path}")

if __name__ == "__main__":
    input_pdf = input("Por favor, ingresa el nombre del documento que vas a separar: ")  # Reemplaza con el nombre de tu archivo PDF de entrada
    output_folder = "salida"      # Carpeta donde se guardarán los archivos individuales
    
    split_pdf(input_pdf, output_folder)