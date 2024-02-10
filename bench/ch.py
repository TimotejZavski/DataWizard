from openai import OpenAI
import json
import re
import subprocess
import sys
import os
import glob
import time


kljuc = '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'
client = OpenAI(api_key=kljuc)
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
Task = '''Histogram for Price Distribution: Display the distribution of house prices to understand the price range. '''



while True:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview", 
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": Task}
            ]
        )
        response = response.choices[0].message.content

        print("Response je tukaj.")

        def overwrite_file(file_path, new_content):
            with open(file_path, 'w') as file:
                file.write(new_content)

        file_path = "t.py"
        match = re.search(r"```(?:\bpython\b)?(.*?)```", response, re.DOTALL)

        #vse mora bit tukaj not
        if match:
            new_content = r_code = match.group(1)

            overwrite_file(file_path, new_content)
            
            try:
                result = subprocess.run(["python", "/Users/timzav/Desktop/t.py"], capture_output=True, text=True)
                error_message = result.stderr
            except subprocess.CalledProcessError as e:
                error_message = str(e)
                Task = f"Error in python script execution: {error_message}"
                continue
            
            print(response)
            Task = input()
        else:
            print("Napaka No python code found.")
