import os
import openai

# entregamos la apikey
api_key = "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"
openai.api_key = api_key

# la ruta a la carpeta con codigos malos 
buggy_codes_path = "icpc2021programs/py/buggy"

# la ruta a la carpeta de codigos fixeados
fixed_codes_path = "fixed-programs"

lista = os.listdir(buggy_codes_path)
print(lista)