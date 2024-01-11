import pandas as pd
import seaborn as sns
import os
import json


def open_file(file_name, bug_type, index):
    if (file_name.startswith("A") or file_name.startswith("J") or file_name.startswith('L')) and index < 10:
        relative_path = f"results/py/{file_name}/fixed-{file_name}_0{index}_{bug_type}.py.json"
        with open(relative_path, "r") as file:
            data = json.load(file)
        return data
    else:
        relative_path = f"results/py/{file_name}/fixed-{file_name}_{index}_{bug_type}.py.json"
        with open(relative_path, "r") as file:
            data = json.load(file)
        return data

def process_data(data):
    keys = sorted(data.keys())
    models = ['gpt-3.5-turbo', 'gpt-4']
    prompts = ['context', 'input', 'context_input']
    results = {}
    for m in models:
        for p in prompts:
            for k in reversed(keys):
                if m in k and p in k:
                    new_data = data[k].split(" ")
                    results[f"{m} - {p}"] = (int(new_data[0]), int(new_data[4]) // 2)
                    
    print(results)
    return results


def analize_bug(bug_type, index):
    programs = os.listdir(f"results/py")
    programs.sort()
    bug_data = []
    for program in programs:
        fixes = os.listdir(f"results/py/{program}")
        for fix in fixes:
            if bug_type in fix:
                print(f"Analizing {program} - {fix}")
                data = open_file(program, bug_type, index)
                bug_data.append(process_data(data))
    df = pd.DataFrame(bug_data)
    if len(df) > 7:
        df = df.drop(df.index[-1])
    if len(df) == 7:
        df['program'] = programs
    df['bug-type'] = bug_type
    return df


def analize_program():
    pass


if __name__ == "__main__":
    bugs = ['SDIF', 'SIIF', 'SRIF', 'SIRT', 'SDIB', 'SDLA', 'SISA', 'SDFN',
            'SISF', 'SMOV', 'SMVB', 'ORRN', 'OLLN', 'OILN', 'OEDE', 'OICD',
            'OAAN', 'OAIS', 'OAID', 'OMOP', 'OFFN', 'OFPF', 'OFPO', 'OICT',
            'DRVA', 'DRWV', 'DMAA', 'DRAC', 'HDMS', 'HIMS']
    df = None
    i = 1
    for bug in bugs:
        df_temp = analize_bug(bug, i)
        if df is None:
            df = df_temp
        else:
            df = pd.concat([df, df_temp], ignore_index=True)
        i += 1
        if i == 10 or i == 25 or i == 27 or i == 32:
            i += 1
        
    df.to_csv("results.csv")
    

    pass
