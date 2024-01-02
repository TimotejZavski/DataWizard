import os
from openai import OpenAI
import json
import re # regular eskspresion za extract code v stringu
import subprocess # za runnat script


client = OpenAI(api_key="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")

data_path = '/Users/timzav/Documents/SpletniPortalZaAnaliziranjeCSVDatotek/r-scripts/datasets/fast_food/BalajiFastFoodSales.json'
explain_path = '/Users/timzav/Documents/SpletniPortalZaAnaliziranjeCSVDatotek/r-scripts/datasets/fast_food/explenation_food.txt'
r_file_path = "/Users/timzav/Desktop/run.R"


#first 10 blocks
def read_first_3_blocks(data_path):
    with open(data_path, 'r') as file:
        data = json.load(file)
    first_10_blocks = data[:3]

    return first_10_blocks


result = read_first_3_blocks(data_path)


with open(explain_path, 'r') as file:
    explain = file.read()

context = f"""
You are an excellent programmer who writes code in R language, using libraries jsonlite and ggplot2. Your response consists of only code, code is withouth any comments
or code explenation. Code should always be like this ```r you generated code ``` or ```R code that you generate ```
I am giving you explenation of data, location of data and sample of data. 
Here is the data:\n\n{result}\n\nand here is an explanation of the data:\n\n{explain}
Data is at this location: {data_path}. Result of your script should be png image/s. After you give me code I will run it and check it for possible errors, if any i will give 
them to you so you understand what is wrong with the code, to fix it in same style of writing as you did before.
"""



while True:
    question = input("\033[92mAsk ChatGPT something: \033[0m")
    if question == "e":
        break

    response = client.chat.completions.create(
        model="gpt-4-1106-preview", 
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": question}
        ]
    )
    response = response.choices[0].message.content
    print("Response", response)

    match = re.search(r"```[Rr](.*?)```", response, re.DOTALL)
    if match:
        r_code = match.group(1)
    else:
        raise ValueError("No R code found in the input string")

    with open(r_file_path, "w") as r_file:
        r_file.write(r_code)

    try:
        # Run R script and capture the error message
        result = subprocess.run(["Rscript", r_file_path], stderr=subprocess.PIPE, text=True)

        # Check if there was an error
        if result.returncode != 0:
            error_message = result.stderr
            print(f"Error in R script execution: {error_message}")
            context = error_message
        else:
            print("R script executed successfully.")
    except subprocess.CalledProcessError as e:
        # Handle the case where the R script crashes
        print(f"R script crashed with error: {e.stderr}")
        zacasen = e.stderr
    except Exception as e:
        # Handle other exceptions that might occur
        print(f"An unexpected error occurred: {e}")
        zacasen = str(e)