import json
import subprocess
import os

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
            print(f"Error en la ejecución del script: {result.stderr}")
            return False
        
        return result.stdout.strip() == expected_output.strip()
        
    except subprocess.TimeoutExpired:
        print("El proceso excedió el tiempo límite de 20 segundos.")
        return False
    except Exception as e:
        print(f"Error al ejecutar la prueba: {e}")
        return False




for folder in folders:
    print(f"testeando la carpeta programs/{folder}")
    codigos = os.listdir(f"programs-fixed/{folder}")
    
    if codigos:
        for codigo in codigos:
            counter = 0
            print(f"Probando el programa {codigo}")
            for filename in os.listdir(f"icpc2021data/{folder}"):
                if filename.endswith('.in'):
                    basename = filename[:-3]
                    input_file = os.path.join(f"icpc2021data/{folder}", basename + '.in')
                    expected_output_file = os.path.join(f"icpc2021data/{folder}", basename + '.ans')

                    if os.path.exists(expected_output_file):
                        test_result = run_test(input_file, expected_output_file, codigo, folder)
                        if test_result:
                            counter += 1
            print(f"El programa {codigo} paso {counter} de {len(os.listdir(f'icpc2021data/{folder}'))} casos de prueba")

    else:
        print(f"No existen codigos arreglados en programs-fixed/{folder}")
    print("\n")