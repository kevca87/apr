import os
import openai
from get_code import get_code
from dotenv import load_dotenv
from colorama import Fore, Style
from tqdm import tqdm

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Funciones para imprimir mensajes de manera estilizada
def print_info(message):
    print(Fore.BLUE + "[INFO] " + Style.RESET_ALL + message)

def print_warning(message):
    print(Fore.YELLOW + "[WARNING] " + Style.RESET_ALL + message)

def print_error(message):
    print(Fore.RED + "[ERROR] " + Style.RESET_ALL + message)

def print_success(message):
    print(Fore.GREEN + "[SUCCESS] " + Style.RESET_ALL + message)

# Configuración de las variables de entorno
api_key = os.getenv("API_KEY")
buggy_codes_path = os.getenv("BUGGY_CODES_PATH")
fixed_codes_path = os.getenv("FIXED_CODES_PATH")
model_name = os.getenv("MODEL_NAME")

# Configurar la API key de OpenAI
openai.api_key = api_key

# Procesar las carpetas con códigos con errores
buggy_programs_folders = os.listdir(buggy_codes_path)

for folder in tqdm(buggy_programs_folders, desc="Procesando carpetas"):

    # Construir la ruta al archivo de contexto
    context_file_path = os.path.join("anexos", "contexts", f"{folder}.txt")

    try:
        # Abrir y leer el archivo de contexto
        with open(context_file_path, 'r') as file:
            context = file.read()

    except Exception as e:
        print_error(f"Error al leer el archivo de contexto para la carpeta {folder}: {e}")


    print_info(f"Arreglando códigos de la carpeta {folder}")
    print_info(f"Contexto para la carpeta: {context}")

    with open(f"anexos/contexts/{folder}.txt", 'r') as file:
        context = file.read()

    codigos = os.listdir(os.path.join(buggy_codes_path, folder))

    if codigos:
        for codigo in tqdm(codigos, desc="Arreglando códigos", leave=False):
            try:
                # Leer el contenido del archivo
                with open(os.path.join(buggy_codes_path, folder, codigo), 'r') as file:
                    content = file.read()

                # Definir los mensajes para la API
                messages = [
                    {"role": "system", "content": "Reparación de código"},
                    {"role": "user", "content": f"context: {context}\nfix the code, just give me back the code and no comments:\n{content}"}
                ]

                # Realizar la solicitud a la API
                response = openai.ChatCompletion.create(
                    model=model_name,
                    messages=messages
                )

                # Obtener la corrección del código
                correccion = response['choices'][0]['message']['content']
                
                # Guardar el código corregido
                get_code(correccion, os.path.join(fixed_codes_path, folder, f"fixed-{codigo}"))

            except Exception as e:
                print_error(f"Error al procesar {codigo}: {e}")
            
            # Espacio después de cada archivo (opcional)
            print("\n")

        # Separador después de procesar todos los archivos en una carpeta
        print("\n" + "-" * 50 + "\n")

    else:
        print_warning(f"No hay códigos en la carpeta {folder}")
        # Separador si la carpeta está vacía
        print("\n" + "-" * 50 + "\n")

print_success("Proceso completado exitosamente!")
