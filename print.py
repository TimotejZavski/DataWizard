from openai import OpenAI
import json
import re
import subprocess
import sys
import os
import glob
import time

#api
with open('/Users/timzav/Desktop/test/config.json') as f:
    config = json.load(f)
    kljuc = config['API_KEY']
    client = OpenAI(api_key=kljuc)

#dobivanje iz c#
if len(sys.argv) > 1:
    inputs = ' '.join(sys.argv[1:])
    Task = ' '.join(sys.argv[-1:])

"""manjka def tokens_in():"""

def tokens_out(input_string, token_length=4):
    count = 0
    for i in range(0, len(input_string), token_length):
        count += 1
    return count

st = 1#za napake stet, kasnej break
zacasen = ""# ce je napaka je to task

def files_list(folder_path):
    file_names = []
    
    # Check if the folder path exists
    if os.path.exists(folder_path):
        # Loop through all files in the folder
        for filename in os.listdir(folder_path):
            # Check if it's a file (not a directory)
            if os.path.isfile(os.path.join(folder_path, filename)):
                file_names.append(filename)
    
    return file_names

def skupek_imen():
    file_names_list = files_list(folder_path)
    file_names_string = ' '.join(file_names_list)

    return file_names_string

folder_path = '/Users/timzav/Desktop/test/test/wwwroot/p_images/'
context = f"You code in python using plotly, matplotlib, seaborn and pandas. Respond with only code inside ```python ``` with no comments. Given {inputs}, save resulting png images to '/Users/timzav/Desktop/test/test/wwwroot/images/'. Images should be name after what tile of chart."

while True:
    s_time = time.time()

    if st <= 3:#3 krat lahka nardi napako
        response = client.chat.completions.create(
            model="gpt-4-1106-preview", 
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": Task}
            ]
        )
        response = response.choices[0].message.content

        #cas
        e_time = time.time()
        r_time = e_time - s_time 

        token_count = tokens_out(response, token_length=4)
        print(f"Number of tokens (received): {token_count}........... v {r_time} sekundah")

        match = re.search(r"```(?:\bpython\b)?(.*?)```", response, re.DOTALL)
        if match:
            r_code = match.group(1)
        else:
            raise ValueError("No python code found in the input string")
        
        p_file_Path = "/Users/timzav/Desktop/test/tplot.py"
        with open(p_file_Path, "w") as r_file:
            r_file.write(r_code)
        
        # Check za ERROR
        try:
            result = subprocess.run(['/Users/timzav/miniconda3/bin/python', p_file_Path], stderr=subprocess.PIPE, text=True)

            #R1
            if result.returncode != 0:
                error_message = result.stderr
                print(f"R1:{skupek_imen}")#Error in python script execution: {error_message}
                Task = f"'{str(e)}' + ', there are this many files already saved:'{skupek_imen}', generate code for only the rest of images that didn't get to be created"
                st = st + 1

            else:
                print(f"Python script executed successfully. Attempts:'{st}'")
                break
            #R2  
        except subprocess.CalledProcessError as e:
            print(f"R2:{skupek_imen}")#Tryes:'{st}'.Python script crashed with error: '{e.stderr}'
            st = st + 1
            Task = f"'{str(e)}' + ', there are this many files already saved:'{skupek_imen}', generate code for only the rest of images that didn't get to be created"
            #R3
        except Exception as e:
            print(f"R3:{skupek_imen}")#f"Tryes:'{st}'. An unexpected error occurred: '{e}'
            st = st + 1
            Task = f"'{str(e)}' + ', there are this many files already saved:'{skupek_imen}', generate code for only the rest of images that didn't get to be created"
            
    else:
        print(f"Attempts:'{st}'. Gave up at 3rd.sk:{skupek_imen()}")
        break

#ciscenje
folder_path = '/Users/timzav/Desktop/test/test/wwwroot/uploads/'
if os.path.exists(folder_path):
    file_paths = glob.glob(os.path.join(folder_path, '*'))
    for file_path in file_paths:
        if os.path.isfile(file_path):
            os.remove(file_path)

