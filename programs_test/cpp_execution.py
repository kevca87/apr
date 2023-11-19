import subprocess

def compile_cpp(program_file:str, executable_file = None) -> None:
    error_file = program_file.replace(".cpp",".err")
    if executable_file == None:
        executable_file = program_file.replace(".cpp",".exe")
    # print(f"g++ {program_file} -o {executable_file}")
    result = subprocess.run(["g++",f"{program_file}", "-o", f"{executable_file}"],stderr=subprocess.PIPE)
    # Save error to file just if an error occurred (returncode != 0), attention to stderr up there
    if result.returncode != 0:
        with open(error_file, "w") as f:
            f.write(result.stderr.decode())

def run_cpp(executable:str,input_file:str,output_file:str) -> None:
    subprocess.run(f"./{executable}",stdin=open(input_file,"r"),stdout=open(output_file,"w"),stderr=open(output_file,"w"))