import json
import os
import datetime

def save_results_as_json(folder, codigo, tests_passed, total_tests, modelo):
    results_folder = f"Results/py/{folder}"
    os.makedirs(results_folder, exist_ok=True)
    file_path = f"{results_folder}/{codigo}.json"

    result_status = "Correctamente arreglado" if tests_passed == total_tests else "Codigo mal arreglado"

    # Crear una entrada con marca de tiempo
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_key = f"{codigo} - {timestamp} - {modelo}"
    results_data = {
        entry_key: f"{tests_passed} codigos pasados de {total_tests} total. Estado: {result_status}"
    }

    # Cargar datos existentes, si existen
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
        existing_data.update(results_data)
    else:
        existing_data = results_data

    # Guardar el archivo JSON actualizado
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)

def print_header(title):
    print(f"\n{'=' * 50}\n{title}\n{'=' * 50}")

def print_test_result(program_name, passed_tests, total_tests):
    print(f"El programa '{program_name}' pasó {passed_tests} de {total_tests} casos de prueba")

def print_error(error_msg):
    print(f"ERROR: {error_msg}")

def print_summary(total_tests, total_passed):
    print(f"\nRESUMEN: De {total_tests} pruebas, {total_passed} fueron exitosas.")
