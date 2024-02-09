from openai import OpenAI
import json
import re
import subprocess
import sys
import os
import glob
import time

#api
with open('/Users/timzav/Desktop/DataWizard/config.json') as f:
    config = json.load(f)
    kljuc = config['API_KEY']
    client = OpenAI(api_key=kljuc)

#dobivanje iz c#
if len(sys.argv) > 1:
    inputs = ' '.join(sys.argv[1:])
    Task = ' '.join(sys.argv[-1:])
    select_color = ' '.join(sys.argv[-1:])

"""manjka def tokens_in():"""#mora bit za not, ven in skupaj

def tokens_in(Task, context):
    total_tokens = len(Task) + len(context)
    return total_tokens // 4

def tokens_out(input_string, token_length=4):
    count = 0
    for _ in range(0, len(input_string), token_length):
        count += 1
    return count

st = 0#za napake stet, kasnej break
zacasen = ""# ce je napaka je to task

#file names list
def files_list(folder_path):
    file_names = []
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                file_names.append(filename)
    return file_names


def skupek_imen():
    file_names_list = files_list(folder_path)#iz funkcije
    file_names_string = ' '.join(file_names_list)
    return file_names_string

folder_path = '/Users/timzav/Desktop/DataWizard/test/wwwroot/images/'
context = f'''Respond with code ONLY simple and plain Python code, no comments/explanations. Result of your code must always be generated png images/charts based on given:
  {inputs}, COLLOR PALLETE of chart must be:'monochrome blue palettes', RESOLUTION of chart(png image) must be:1920x1080
  Save the charts as high-resolution PNG images to the '{folder_path}'.
  '''

while True:
    if st <= 4:#3 krat lahka nardi napako
        #s_time = time.time()
        response = client.chat.completions.create(
            model="gpt-4-1106-preview", 
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": Task}
            ]
        )
        response = response.choices[0].message.content

        #cas #imena so mela smisel - ne vec - ponovno majo, cas ga nima
        """
        e_time = time.time()
        r_time = e_time - s_time
        rounded_time_difference = round(r_time.total_seconds())

        token_count = tokens_out(response, token_length=4)
        print(f"Number of tokens (received): {token_count}, v {r_time} sekundah\n")
        """
        
        match = re.search(r"```(?:\bpython\b)?(.*?)```", response, re.DOTALL)

        #pattern in string? #0
        if match:
            r_code = match.group(1)
        else:
            raise ValueError(f"No python code found in the input string{response}")
        
        #zapis kode
        p_file_Path = "/Users/timzav/Desktop/DataWizard/tplot.py"
        with open(p_file_Path, "w") as r_file:
            r_file.write(r_code)
        
        # Check za ERROR
        try:
            result = subprocess.run(['/Users/timzav/miniconda3/bin/python', p_file_Path], stderr=subprocess.PIPE, text=True)

            #R1
            if result.returncode != 0:
                e = str(result.stderr)
                print(f"R1:{skupek_imen}")#Error in python script execution: {e}
                task = f'''This code:'{response}, generated only this images:'{skupek_imen()}' and gave this error:'{str(e)}' generate code for only the rest of images that didn't get to be created by given code.'''
                st = st + 1 
            else:
                print(f"Python script executed successfully in {st} attempt")
                break
            #R2  
        except subprocess.CalledProcessError as e:
            print(f"R2:{skupek_imen}")#Tryes:'{st}'.Python script crashed with error: '{e.stderr}'
            task = f'''This code:'{response}, generated only this images:'{skupek_imen()}' and gave this error:'{str(e)}' generate code for only the rest of images that didn't get to be created by given code.'''
            st = st + 1
            #R3
        except Exception as e:
            print(f"R3:{skupek_imen}")#f"Tryes:'{st}'. An unexpected error occurred: '{e}'
            task = f'''This code:'{response}, generated only this images:'{skupek_imen()}' and gave this error:'{str(e)}' generate code for only the rest of images that didn't get to be created by given code.'''
            st = st + 1

    else:

        print(f"Attempts:'{st}'. Gave up at 4rd. imena\n:{skupek_imen()}")
        print(f"token out:{tokens_out(response, token_length=4)}")
        print(f"{tokens_in(Task, context)}")
        break
     


#upload ciscenje-folder 
    #safety
folder_path = '/Users/timzav/Desktop/DataWizard/test/wwwroot/uploads/'
if os.path.exists(folder_path):
    file_paths = glob.glob(os.path.join(folder_path, '*'))
    for file_path in file_paths:
        if os.path.isfile(file_path):
            os.remove(file_path)
#varnostno
#tplot ciscenje-datoteka
with open(p_file_Path, 'w'):
   pass

