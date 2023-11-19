import subprocess
import os

def read_file(file_name) -> str:
    with open(file_name, "r") as f:
        return f.read()

def equal_outputs(out_file_A:str,out_file_B:str) -> bool:
    return read_file(out_file_A) == read_file(out_file_B)

def test_equals_true(out_file_tested:str,out_file_reference:str) -> bool:
    test_answer = equal_outputs(out_file_tested,out_file_reference)
    if test_answer:
        print(f"TEST PASSED: {out_file_tested}")
    else:
        print(f"TEST FAILED: {out_file_tested}")
    return int(test_answer)

def compile_cpp(program_file:str, executable_file = None) -> None:
    if executable_file is None:
        executable_file = program_file.split(".")[0]
    subprocess.run(["g++",f"{program_file}", "-o", f"{executable_file}.exe"])

def run_cpp(executable:str,input_file:str,output_file:str) -> None:
    subprocess.run(f"./{executable}",stdin=open(input_file,"r"),stdout=open(output_file,"w"))

if __name__ == "__main__":
    compile_cpp("icpc2021programs/reference/A-cross/A-cross.cpp")
    run_cpp("icpc2021programs/reference/A-cross/A-cross.exe","icpc2021data/A-cross/sample-1.in","icpc2021programs/reference/A-cross/A-cross.out")
    print(test_equals_true("icpc2021programs/reference/A-cross/A-cross.out","icpc2021data/A-cross/sample-1.ans"))