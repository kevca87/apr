def get_code(correcion, path):
    if ("´´´" in correcion and "python" not in correcion):
        correcion = correcion.split("´´´")[1]

    elif ("´´´" in correcion and "python" in correcion):
        correcion = correcion.split("´´´")[1]
        correcion = correcion.split("python")[1]
    
    with open(path, "w") as file:
        file.write(correcion)
    return True