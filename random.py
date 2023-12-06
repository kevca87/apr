import os
from colorama import Fore, Style
from tqdm import tqdm

def print_info(message):
    print(Fore.BLUE + "[INFO] " + Style.RESET_ALL + message)

def print_warning(message):
    print(Fore.YELLOW + "[WARNING] " + Style.RESET_ALL + message)

def print_error(message):
    print(Fore.RED + "[ERROR] " + Style.RESET_ALL + message)

def print_success(message):
    print(Fore.GREEN + "[SUCCESS] " + Style.RESET_ALL + message)

# Ejemplo de uso
print_info("Iniciando el proceso de corrección...")
print_warning("Este proceso puede tardar varios minutos.")
# ... tu código ...
print_success("Proceso completado exitosamente!")
