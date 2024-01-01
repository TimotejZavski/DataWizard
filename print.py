from openai import OpenAI
import json
import re # regular eskspresion za extract code v stringu
import subprocess # za runnat script
import sys #variable pass
import os

client = OpenAI(api_key="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")
p_file_Path = "/Users/timzav/Desktop/test/tplot.py"

if len(sys.argv) > 1:#dobivanje iz c#
    inputs = ' '.join(sys.argv[1:])
    Task = ' '.join(sys.argv[-1:])

    context = f"""
You code in python using plotly, matplotlib, seaborn and pandas. Respond with only code inside ```python ``` with no comments.
Given {inputs}, save resulting png images to '/Users/timzav/Desktop/test/test/wwwroot/p_images/'.
    """

def count_tokens(input_string, token_length=4):
    count = 0
    for i in range(0, len(input_string), token_length):
        count += 1
    return count

st = 1#za napake stet, kasnej break
zacasen = ""# ce je napaka je to task

def list_files_in_folder(folder_path):
    file_names = []
    
    # Check if the folder path exists
    if os.path.exists(folder_path):
        # Loop through all files in the folder
        for filename in os.listdir(folder_path):
            # Check if it's a file (not a directory)
            if os.path.isfile(os.path.join(folder_path, filename)):
                file_names.append(filename)
    
    return file_names


folder_path = '/Users/timzav/Desktop/test/test/wwwroot/p_images/'



while True:
    if st <= 3:#3 krat lahka nardi napako
        response = client.chat.completions.create(
            model="gpt-4-1106-preview", 
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": Task}
            ]
        )
        response = response.choices[0].message.content

        token_count = count_tokens(response, token_length=4)
        print(f"Number of tokens (received): {token_count}")

        match = re.search(r"```(?:\bpython\b)?(.*?)```", response, re.DOTALL)
        if match:
            r_code = match.group(1)
        else:
            raise ValueError("No python code found in the input string")
        

        with open(p_file_Path, "w") as r_file:
            r_file.write(r_code)

        try:
            result = subprocess.run(['/Users/timzav/miniconda3/bin/python', p_file_Path], stderr=subprocess.PIPE, text=True)

            # Check if there was an error
            if result.returncode != 0:
                error_message = result.stderr
                print(f"Error in python script execution: {error_message}")
                file_names_list = list_files_in_folder(folder_path)
                file_names_string = ' '.join(file_names_list)
                Task = f"{error_message} There are this many files already saved: {file_names_string}"
                st = st + 1

            else:
                print(f"Python script executed successfully. F:'{st}'")
                break
        except subprocess.CalledProcessError as e:
            # Handle the case where the R script crashes
            print(f"F:'{st}'.Python script crashed with error: '{e.stderr}'")
            file_names_list = list_files_in_folder(folder_path)
            file_names_string = ' '.join(file_names_list)
            st = st + 1
            Task = f"{e.stderr} 'there are this many files already saved: {file_names_string}"
        except Exception as e:
            # Handle other exceptions that might occur
            print(f"F:'{st}'.An unexpected error occurred: '{e}'")
            file_names_list = list_files_in_folder(folder_path)
            file_names_string = ' '.join(file_names_list)
            st = st + 1
            Task = f"{str(e)} + 'there are this many files already saved: {file_names_string}"
            
    else:
        print(f"F:'{st}'.Execution failed after 3 tryes.")
        break
        


