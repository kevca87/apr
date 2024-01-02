import json
import subprocess
import os
from functions import save_results_as_json, print_header, print_test_result, print_error, print_summary
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()
model_name = os.getenv("MODEL_NAME")


total_tests_run = 0
total_tests_passed = 0

folders = os.listdir("programs-fixed")


def run_test(input_file, expected_output_file, codigo, folder):
    try:
        with open(input_file, 'r') as infile, open(expected_output_file, 'r') as outfile:
            input_text = infile.read()
            for line in input_text.split('\n'):
                if line.startswith('#'):
                    input_text = input_text.replace(line, '')
            input_text.join('\n')
            expected_output = outfile.read()
        
        result = subprocess.run(
            ['python', f"programs-fixed/{folder}/{codigo}"],
            input=input_text,
            text=True,
            capture_output=True,
            timeout=20
        )

        if result.returncode != 0:
            # print(f"Error en la ejecución del script: {result.stderr}")
            return False
        
        return result.stdout.strip() == expected_output.strip()
        
    except subprocess.TimeoutExpired:
        # print("El proceso excedió el tiempo límite de 20 segundos.")
        return False
    except Exception as e:
        # print(f"Error al ejecutar la prueba: {e}")
        return False



for folder in folders:
    print_header(f"Testeando la carpeta programs/{folder}")
    codigos = os.listdir(f"programs-fixed/{folder}")
    folder_tests_run = 0
    folder_tests_passed = 0

    if codigos:
        for codigo in codigos:
            print(f"\nProbando el programa '{codigo}'")
            program_tests_passed = 0
            total_tests_for_program = len(os.listdir(f'icpc2021data/{folder}'))


            for filename in os.listdir(f"icpc2021data/{folder}"):
                if filename.endswith('.in'):
                    folder_tests_run += 1
                    total_tests_run += 1
                    basename = filename[:-3]
                    input_file = os.path.join(f"icpc2021data/{folder}", basename + '.in')
                    expected_output_file = os.path.join(f"icpc2021data/{folder}", basename + '.ans')

                    if os.path.exists(expected_output_file):
                        test_result = run_test(input_file, expected_output_file, codigo, folder)
                        if test_result:
                            program_tests_passed += 1
                            folder_tests_passed += 1
                            total_tests_passed += 1
            
            print_test_result(codigo, program_tests_passed, len(os.listdir(f'icpc2021data/{folder}')))
            save_results_as_json(folder, codigo, program_tests_passed, total_tests_for_program, model_name)

    else:
        print("No existen códigos arreglados en esta carpeta.")

    print_summary(folder_tests_run, folder_tests_passed)

print_summary(total_tests_run, total_tests_passed)