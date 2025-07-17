# ast_parser_q17.py

import ast

def analyze_functions_q17(source_path_q17):
    with open(source_path_q17, "r") as f_q17:
        tree_q17 = ast.parse(f_q17.read(), filename=source_path_q17)

    functions_q17 = [node for node in tree_q17.body if isinstance(node, ast.FunctionDef)]
    for func_q17 in functions_q17:
        name_q17 = func_q17.name
        args_q17 = [arg.arg for arg in func_q17.args.args]
        doc_q17 = ast.get_docstring(func_q17) or "<no docstring>"
        num_statements_q17 = len(func_q17.body)
        print(f"Function: {name_q17}")
        print(f"  Arguments: {args_q17}")
        print(f"  Docstring: {doc_q17!r}")
        print(f"  Number of top-level statements: {num_statements_q17}")
        print()