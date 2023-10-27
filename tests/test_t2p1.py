# import importlib
# name_file_module_to_test = "P1.abisai.code"
# file_module_to_test = importlib.import_module(name_file_module_to_test)

# encontrar_elemento_mas_repetido = getattr(file_module_to_test,"encontrar_elemento_mas_repetido")

# from code import encontrar_elemento_mas_repetido

import os
import pytest
from import_utils import import_function

files = list(map(lambda dir_name: f'./P1/{dir_name}/code.py' ,os.listdir('./P1')))

@pytest.mark.parametrize("file_path", files)
def test_encontrar_elemento_mas_repetido_tc01(file_path):
    fun_name = "encontrar_elemento_mas_repetido"
    encontrar_elemento_mas_repetido = import_function(fun_name,file_path)
    lista = ["Monopoly", "Catan", "Cachos", "Monopoly"]
    assert encontrar_elemento_mas_repetido(lista)  == "Monopoly"

@pytest.mark.parametrize("file_path", files)
def test_encontrar_elemento_mas_repetido_tc02(file_path):
    fun_name = "encontrar_elemento_mas_repetido"
    encontrar_elemento_mas_repetido = import_function(fun_name,file_path)
    lista = ["Catan", "Cachos", "Monopoly"]
    assert encontrar_elemento_mas_repetido(lista)  == "Catan"

@pytest.mark.parametrize("file_path", files)
def test_eliminar_elementos_tc01(file_path):
    fun_name = "eliminar_elementos"
    eliminar_elementos = import_function(fun_name,file_path)
    assert eliminar_elementos(["Monopoly", "Cachos", "Monopoly", "Cachos", "Pictionary"], "Monopoly")  == ["Cachos", "Cachos", "Pictionary"]