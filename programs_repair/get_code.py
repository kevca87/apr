def get_code(correcion, path):
    if ("```" in correcion and "python" not in correcion):
        correcion = correcion.split("```")[1]

    if ("```" in correcion and "python" in correcion):
        correcion = correcion.split("```")[1]
        correcion = correcion.split("python")[1]
    
    if ("```" in correcion):
        correcion = correcion.split("```")[1]

    if ("Here is the fixed code:" in correcion):
        correcion = correcion.split("Here is the fixed code:")[1]
    
    if ("Here's the fixed code:" in correcion):
        correcion = correcion.split("Here is the fixed code:")[1]
    
    if ("Fixed code:" in correcion):
        correcion = correcion.split("Here is the fixed code:")[1]
    
    with open(path, "w") as file:
        file.write(correcion)
    return True