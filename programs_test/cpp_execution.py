import subprocess

def compile_cpp(program_file:str, executable_file = None) -> None:
    if executable_file is None:
        executable_file = program_file.split(".")[0]
    subprocess.run(["g++",f"{program_file}", "-o", f"{executable_file}.exe"])

def run_cpp(executable:str,input_file:str,output_file:str) -> None:
    subprocess.run(f"./{executable}",stdin=open(input_file,"r"),stdout=open(output_file,"w"))