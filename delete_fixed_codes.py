import os
import shutil

def delete_files_in_subfolders(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f'Archivo eliminado: {file_path}')

decision = str(input("estas seguro de eliminar todos los codigos arreglados? (y/n): "))
if decision == 'yes' or decision == 'y':
    delete_files_in_subfolders('programs-fixed')
else:
    print("no se elimino ningun archivo")
