from cpp_execution import compile_cpp, run_cpp
import os

def read_file(file_name) -> str:
    with open(file_name, "r") as f:
        return f.read()

def equal_outputs(out_file_A:str,out_file_B:str) -> bool:
    return read_file(out_file_A) == read_file(out_file_B)

def test_equals_true(out_file_tested:str,out_file_reference:str,print_result=True) -> bool:
    test_answer = equal_outputs(out_file_tested,out_file_reference)
    if print_result:
        if test_answer:
            print(f"TEST PASSED: {out_file_tested}")
        else:
            print(f"TEST FAILED: {out_file_tested}")
    return int(test_answer)

if __name__ == "__main__":

    reference_dir = "..\\icpc2021programs\\cpp\\reference"
    data_dir = "..\\icpc2021data"
    for dirpath, dirnames, filenames in os.walk(reference_dir):
        # print(f'Visited directory: {dirpath}')
        # print(f'Subdirectories: {dirnames}')
        # print(f'Files: {filenames}')
        for filename in filenames:
            # print(dirpath.split("\\"))
            problem_name = dirpath.split("\\")[-1]
            if filename.endswith(".cpp"):
                try:
                    file_path = os.path.join(dirpath, filename)
                    compile_cpp(file_path)
                    # input_dir = os.path.join(data_dir,problem_name)
                    # input_file = os.path.join(input_dir,"sample-1.in")
                    # run_cpp(file_path.replace(".cpp",".exe"),input_file,file_path.replace(".cpp",".out"))
                except Exception as e:
                    print(f"ERROR: {file_path}")
                    print(e)
                # test_equals_true(file_path.replace(".cpp",".out"),file_path.replace(".cpp",".ans"))
    # compile_cpp("icpc2021programs/reference/A-cross/A-cross.cpp")
    # run_cpp("icpc2021programs/reference/A-cross/A-cross.exe","icpc2021data/A-cross/sample-1.in","icpc2021programs/reference/A-cross/A-cross.out")
    # print(test_equals_true("icpc2021programs/reference/A-cross/A-cross.out","icpc2021data/A-cross/sample-1.ans"))