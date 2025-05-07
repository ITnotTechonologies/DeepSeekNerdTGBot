from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()
ai_token = os.getenv('DEEPSEEK_TOKEN')
print(ai_token)



client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=ai_token,
)

LanguagesCodes = ['en', 'ru', 'fr', 'de', 'uk', 'ru', 'es', 'pl']

for Code in LanguagesCodes:
    s = str()
    with open('welcome_message/welcome_en.txt', 'r', encoding='utf-8') as file:
        s = file.read()
    print(s)
    completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
    extra_body={},
    model="deepseek/deepseek-chat",
    messages=[
    {   
        "role": "user",
        "content": f'Translate the given text into {Code}, as the result output only translated text' + s
        
    }
    ]
    )
    print(completion.choices[0].message.content)
    result = completion.choices[0].message.content
    with open(f'welcome_message/welcome_{Code}.txt', 'w', encoding = 'utf-8') as file:
        file.write(result)