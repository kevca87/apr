import ast

# Open the file for reading
file_path = "./P1/abisai/code.py"  # Replace with the path to your file
with open(file_path, 'r') as file:
    # Read the entire file content
    file_contents = file.read()
    # Print the file content
    filename = 'lol'
    mode = 'exec'
    result = compile(file_contents, filename, mode, ast.PyCF_ONLY_AST)
    # print(result.body[1].__dict__)
    # print(ast.unparse(result.body[1]))
    fun_str = compile(ast.unparse(result.body[1]),'lolazo','exec')
    # print(fun_str)
    # fun = exec(fun_str)
    # print(result.body[1])
    namespace = {}
    exec(fun_str,namespace)
    fun = namespace['encontrar_elemento_mas_repetido']
    print(fun(["Monopoly", "Catan", "Cachos", "Monopoly"]))