import json
import subprocess
import os
import sys
import time 

# Establecer el nuevo límite de recursión

# cambiar al programa que se desea ejecutar
programa = "L-whereami"

# cambiar al directorio donde se encuentran los archivos de prueba

test_directory = f"./icpc2021data/{programa}"



def run_test(input_file, expected_output_file):

    start_time = time.time()

    try:
        with open(input_file, 'r') as infile, open(expected_output_file, 'r') as outfile:
            input_text = infile.read()
            expected_output = outfile.read()

        result = subprocess.run(
            ['python', f"icpc2021programs/py/reference/{programa}.py"],
            input=input_text,
            text=True,
            capture_output=True,
            timeout=70
        )

        if result.returncode != 0:
            print(f"Error en la ejecución del script: {result.stderr}")
            return False, time.time() - start_time

        return result.stdout.strip() == expected_output.strip(), time.time() - start_time

    except subprocess.TimeoutExpired:
        print("El proceso excedió el tiempo límite de 60 segundos.")
        return False, time.time() - start_time
    except Exception as e:
        print(f"Error al ejecutar la prueba: {e}")
        return False, time.time() - start_time


counter = 0
for filename in os.listdir(test_directory):
    if filename.endswith('.in'):
        basename = filename[:-3]
        input_file = os.path.join(test_directory, basename + '.in')
        expected_output_file = os.path.join(test_directory, basename + '.ans')

        if os.path.exists(expected_output_file):
            test_result, duration = run_test(input_file, expected_output_file)
            print(f"Test {basename}: {'PASA' if test_result else 'FALLA'} en {duration:.2f} segundos")
            if test_result:
                counter += 1

print(f"Total de tests pasados: {counter} de {len(os.listdir(test_directory)) // 2}")

