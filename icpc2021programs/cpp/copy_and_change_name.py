import os
import shutil

def copy_and_change_name(reference_dir, buggy_dir, suffixes):
    # Get the list of programs_directories in the reference directory
    programs_directories = [d for d in os.listdir(reference_dir) if os.path.isdir(os.path.join(reference_dir, d))]
    
    # Copy programs_directories and CPP files
    for directory in programs_directories:
        # Create the corresponding directory in the buggy directory
        new_directory = os.path.join(buggy_dir, directory)
        os.makedirs(new_directory, exist_ok=True)

        # Get the path of the CPP file in the reference directory
        cpp_file = os.path.join(reference_dir, directory, directory + '.cpp')
        print(cpp_file)

        # Copy the CPP file for each suffix in the list
        for suffix_index, suffix in enumerate(suffixes):
            # Create the new CPP file name with index
            new_cpp_file = os.path.join(new_directory, f'{directory}_{suffix_index+1:02}_{suffix}.cpp')

            # Copy the CPP file to the new location
            shutil.copy2(cpp_file, new_cpp_file)
    
    print(f'Copied {len(programs_directories)} programs_directories to {buggy_dir}')

def extract_bug_type_suffixes(filename):
    extracted_strings = []
    with open(filename, 'r') as file:
        for line in file:
            start_index = line.find('(')
            end_index = line.find(')')
            if start_index != -1 and end_index != -1:
                extracted_string = line[start_index + 1:end_index]
                extracted_strings.append(extracted_string)
    return extracted_strings


# Example usage
reference_dir = './reference'
buggy_dir = './buggy'
suffixes = extract_bug_type_suffixes('bug_types.txt')

copy_and_change_name(reference_dir, buggy_dir, suffixes)
