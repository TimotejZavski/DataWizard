print("scripta zagnana")
from openai import OpenAI
import json
import re # regular eskspresion za extract code v stringu
import subprocess # za runnat script
import sys #variable pass

client = OpenAI(api_key="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")
r_file_path = "/Users/timzav/Desktop/run.R"

if len(sys.argv) > 1:
    inputs = ' '.join(sys.argv[1:])
    print(inputs)


    context = f"""
    You are an excellent programmer who writes code in R language, using libraries jsonlite and ggplot2. Your response consists of only code, code is withouth any comments
    or code explenation. Code should always be like this ```r you generated code ``` or ```R code that you generate ```
    I am giving you explenation of data, location of data and sample of data. 
    Here is description, task and data path along with data example:{inputs}. Result of your script should be png image/s. After you give me code I will run it and check it for possible errors, if any i will give 
    them to you so you understand what is wrong with the code, to fix it in same style of writing as you did before.
    """
