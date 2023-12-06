import os
import openai
from get_code import get_code

# entregamos la apikey
api_key = "PUT HERE APIKEY"
openai.api_key = api_key

# la ruta a la carpeta con codigos malos 
buggy_codes_path = "icpc2021programs/py/buggy"

# la ruta a la carpeta de codigos fixeados
fixed_codes_path = "programs-fixed"


buggy_programs_folders = os.listdir(buggy_codes_path)

for folfer in buggy_programs_folders:
    print(f"arreglando codigos de la carpeta {buggy_codes_path}/{folfer}")
    codigos = os.listdir(f"{buggy_codes_path}/{folfer}")

    if codigos:
        for codigo in codigos:
            print(f"---- arreglando codigo {buggy_codes_path}/{folfer}/{codigo}")

            # leemos el contenido del archivo
            with open(f"{buggy_codes_path}/{folfer}/{codigo}", 'r') as file:
                # guardamos en contenido en una variable para entregarlo a la API
                content = file.read()

            # definimos los mensajes que se entregarán a la api apra que corrija el código
            messages = [
                {"role": "system", "content": "Reparacion de código"},
                {"role": "user", "content": f"fix the code, just give me back the code and no comments:\n{content}"}
            ]

            # Realiza la solicitud a la API
            response = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",  # Asegúrate de utilizar el nombre del modelo correcto
                messages=messages, # Puedes ajustar este valor según tus necesidades
            )

            # Obtén la corrección del código
            correccion = response['choices'][0]['message']['content']
            
            # guardamos el código arreglado en un archivo
            get_code(correccion, f"{fixed_codes_path}/{folfer}/fixed-{codigo}")



            print("\n")
    else:
        print(f"XXX no hay codigos en la carpeta XXX")
        print("\n")

    