import os
import sys
import shutil
from generate_page import generate_pages_recursive

def copy_static(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_static(s, d)
        else:
            shutil.copy2(s, d)

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    print(f"Limpiando directorio antiguo de salida y copiando estáticos a docs... (Basepath: {basepath})")
    # Al ejecutarse desde la raíz, usamos las rutas directas de las carpetas
    copy_static("static", "docs")
    
    print("Generando páginas de manera recursiva...")
    generate_pages_recursive("content", "template.html", "docs", basepath)
    print("¡Proceso de generación estática completado con éxito!")

if __name__ == "__main__":
    main()
