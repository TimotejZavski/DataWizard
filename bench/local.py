import ollama
from openai import OpenAI
import json
import re
import subprocess
import sys
import os
import glob
import time

context = '''
To this message respond with code ONLY. Code should be simple and to the point in Python language. Point of the code is chart(s)/grapf(s) generation in form of PNG(image).  Code/your whole response that you generate should be inside ```python ```, for example: 
```python 
your generated code/response
```
Now that you understand how to respond to this whole message you are now geting example of data, description, file(json) location and task->what your response/code should do.
Example of data(Example is one json block, one of many json blocks in/from json file. Example of data is given to you so you understand how data inside file looks like, what atribute is what and so on):
{
  "BROKERTITLE": "Brokered by Douglas Elliman  -111 Fifth Ave",
  "TYPE": "Condo for sale",
  "PRICE": "315000",
  "BEDS": "2",
  "BATH": "2",
  "PROPERTYSQFT": "1400",
  "ADDRESS": "2 E 55th St Unit 803",
  "STATE": "New York, NY 10022",
  "MAIN_ADDRESS": "2 E 55th St Unit 803New York, NY 10022",
  "ADMINISTRATIVE_AREA_LEVEL_2": "New York County",
  "LOCALITY": "New York",
  "SUBLOCALITY": "Manhattan",
  "STREET_NAME": "East 55th Street",
  "LONG_NAME": "Regis Residence",
  "FORMATTED_ADDRESS": "Regis Residence, 2 E 55th St #803, New York, NY 10022, USA",
  "LATITUDE": "40.761255",
  "LONGITUDE": "-73.9744834"
},
Description of atributes(so you get idea what data presents):
  BROKERTITLE: Title of the broker
  TYPE: Type of the house
  PRICE: Price of the house
  BEDS: Number of bedrooms
  BATH: Number of bathrooms
  PROPERTYSQFT: Square footage of the property
  ADDRESS: Full address of the house
  STATE: State of the house
  MAIN_ADDRESS: Main address information
  ADMINISTRATIVE_AREA_LEVEL_2: Administrative area level 2 information
  LOCALITY: Locality information
  SUBLOCALITY: Sublocality information
  STREET_NAME: Street name
  LONG_NAME: Long name
  FORMATTED_ADDRESS: Formatted address
  LATITUDE: Latitude coordinate of the house
  LONGITUDE: Longitude coordinate of the house',
FILE PATH:
  /Users/timzav/Desktop/datasets/data/new_york/use_me.json
COLLOR (of chart):
  light blue/green
RESOLUTION (of chart/png image
  1920x1080
Save the charts as high-resolution PNG images to the '/Users/timzav/Desktop/zacasno/'.
'''



#api
with open('/Users/timzav/Desktop/DataWizard/config.json') as f:
    config = json.load(f)
    kljuc = config['API_KEY']
    client = OpenAI(api_key=kljuc)

#dobivanje iz c#
    """
if len(sys.argv) > 1:
    inputs = ' '.join(sys.argv[1:])
    Task = ' '.join(sys.argv[-1:])
    select_color = ' '.join(sys.argv[-1:])
"""
"""manjka def tokens_in():"""#mora bit za not, ven in skupaj


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

while True:
        Task = input("Task: ")
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
        p_file_Path = "/Users/timzav/Desktop/t.py"
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


