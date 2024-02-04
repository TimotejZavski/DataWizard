from openai import OpenAI
import json

with open('/Users/timzav/Desktop/DataWizard/liver.json', 'r') as file:
    json_string = file.read()

def tokens_out(input_string, token_length=4):
    count = 0
    for i in range(0, len(input_string), token_length):
        count += 1
    return count    

if tokens_out(json_string, token_length=4) < 125000:
    with open('/Users/timzav/Desktop/DataWizard/config.json') as f:
        config = json.load(f)
        kljuc = config['API_KEY']
        client = OpenAI(api_key=kljuc)

    context = "You will be provided a big JSON data content and what I need you to do is analyse what data present, important is that you list some fun or interesting facts about that the normal human eye can not cache."
    response = client.chat.completions.create(
                model="gpt-4-1106-preview", 
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": json_string}
                ]
            )
    response = response.choices[0].message.content
    print(response)
else:
    print("bigger than 128k")



"""
128KB = 31883 cca. 32k tokens
128/32=4
4*128=512 = pol mega
"""




