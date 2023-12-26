print("scripta zagnana\n")
from openai import OpenAI
import json
import re # regular eskspresion za extract code v stringu
import subprocess # za runnat script
import sys #variable pass

client = OpenAI(api_key="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")
r_file_path = "/Users/timzav/Desktop/run.R"
if len(sys.argv) > 1:
    inputs = ' '.join(sys.argv[1:])
    Task = ' '.join(sys.argv[-1:])
    print(f"\n{Task}\n")
    context = f"""
    You are an excellent programmer who writes code in R language, using libraries jsonlite and ggplot2. Your response consists of only code, code is withouth any comments
    or code explenation. Code should always be like this ```r you generated code ``` or ```R code that you generate ```
    I am giving you explenation of data, location of data and sample of data. 
    Here is description, task and data path along with data example:{inputs}. Result of your script should be png image/s. After you give me code I will run it and check it for possible errors, if any i will give 
    them to you so you understand what is wrong with the code, to fix it in same style of writing as you did before.
    """
    print("cez context")


while True:
    print("v while loopu")
    response = client.chat.completions.create(
        model="gpt-4-1106-preview", 
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": Task}
        ]
    )
    response = response.choices[0].message.content
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
    break


