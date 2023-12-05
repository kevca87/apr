import json
import subprocess
import os


def print_header(title):
    print(f"\n{'=' * 50}\n{title}\n{'=' * 50}")

def print_test_result(program_name, passed_tests, total_tests):
    print(f"El programa '{program_name}' pasó {passed_tests} de {total_tests} casos de prueba")

def print_error(error_msg):
    print(f"ERROR: {error_msg}")

def print_summary(total_tests, total_passed):
    print(f"\nRESUMEN: De {total_tests} pruebas, {total_passed} fueron exitosas.")


def save_results_as_json(folder, codigo, tests_passed, total_tests):
    results_folder = f"Results/py/{folder}"
    os.makedirs(results_folder, exist_ok=True)
    file_path = f"{results_folder}/{codigo}.json"

    result_status = "Correctamente arreglado" if tests_passed == total_tests else "Codigo mal arreglado"
    results_data = {
        codigo: f"{tests_passed} codigos pasados de {total_tests} total. Estado: {result_status}"
    }

    with open(file_path, "w") as file:
        json.dump(results_data, file, indent=4, ensure_ascii=False)

total_tests_run = 0
total_tests_passed = 0

folders = os.listdir("programs-fixed")


def run_test(input_file, expected_output_file, codigo, folder):
    try:
        with open(input_file, 'r') as infile, open(expected_output_file, 'r') as outfile:
            input_text = infile.read()
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
            save_results_as_json(folder, codigo, program_tests_passed, total_tests_for_program)

    else:
        print("No existen códigos arreglados en esta carpeta.")

    print_summary(folder_tests_run, folder_tests_passed)

print_summary(total_tests_run, total_tests_passed)