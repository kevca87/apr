import ast

def get_fundef_nodes(source_code_str):
    ast_tree = compile(source_code_str, 'does not matter', 'exec', ast.PyCF_ONLY_AST)
    fundef_nodes = []
    fundef_nodes_source = []
    for ast_node in ast_tree.body:
        if type(ast_node).__name__ == 'FunctionDef':
            fundef_nodes.append(ast_node)
            fun_source_code_str = ast.unparse(ast_node)
            fundef_nodes_source.append(fun_source_code_str)
    return {'ast_nodes':fundef_nodes,'source_code':fundef_nodes_source}

def import_function(fun_name, file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        functions_definitions = get_fundef_nodes(file_content)
        source_code = '\n'.join(functions_definitions['source_code'])
        namespace = {}
        code_obj = compile(source_code, 'does not matter', 'exec')
        exec(code_obj,namespace)
        fun_obj = namespace[fun_name]
        return fun_obj