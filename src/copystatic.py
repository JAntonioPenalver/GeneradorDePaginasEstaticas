import os
import shutil

def copy_files_recursive(source_dir, dest_dir):
    """
    Copia recursivamente todos los archivos y directorios 
    desde source_dir hacia dest_dir.
    """
    if not os.path.exists(dest_dir):
        print(f"Creando directorio: {dest_dir}")
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isfile(source_path):
            print(f"Copiando archivo: {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)
        else:
            print(f"Entrando al directorio: {source_path}")
            copy_files_recursive(source_path, dest_path)
