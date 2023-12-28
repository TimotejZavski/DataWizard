print("scripta zagnana\n")
from openai import OpenAI
import json
import re # regular eskspresion za extract code v stringu
import subprocess # za runnat script
import sys #variable pass

client = OpenAI(api_key="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")
p_file_Path = "/Users/timzav/Desktop/test/tplot.py"
if len(sys.argv) > 1:
    inputs = ' '.join(sys.argv[1:])
    Task = ' '.join(sys.argv[-1:])

    context = f"""
    You write code in python, using libraries plotly mathplotlib, seaborn, pandas. Your response consists of only code, withouth comments
    or inside/outside code explenation. Code should always be like this ```python you generated code ``` so inside this brackets.
    For better understanding what you are working with, {inputs}. Watch out for Error in `geom_text()`: and ! Problem while computing aesthetics.
    Result of your script should be png image/s.
    """

def count_tokens(input_string, token_length=4):
    count = 0
    for i in range(0, len(input_string), token_length):
        count += 1
    return count


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
    token_count = count_tokens(response, token_length=4)
    print(f"Number of tokens: {token_count}")
    match = re.search(r"```(?:\bpython\b)?(.*?)```", response, re.DOTALL)
    if match:
        r_code = match.group(1)
    else:
        raise ValueError("No python code found in the input string")

    with open(p_file_Path, "w") as r_file:
        r_file.write(r_code)

    try:
        # Run R script and capture the error message
        result = subprocess.run(['/Users/timzav/miniconda3/bin/python', p_file_Path], stderr=subprocess.PIPE, text=True)


        # Check if there was an error
        if result.returncode != 0:
            error_message = result.stderr
            print(f"Error in python script execution: {error_message}")
            Task = error_message
            
        else:
            print("python script executed successfully.")
    except subprocess.CalledProcessError as e:
        # Handle the case where the R script crashes
        print(f"python script crashed with error: {e.stderr}")
        zacasen = e.stderr
    except Exception as e:
        # Handle other exceptions that might occur
        print(f"An unexpected error occurred: {e}")
        zacasen = str(e)
    break


