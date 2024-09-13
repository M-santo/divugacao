import os
import openai
from groq import Groq
from dotenv import load_dotenv

# Carrega variáveis de ambiente de um arquivo .env
load_dotenv()

openai.api_key = os.getenv("YOUR_OPENAI_API_KEY")

def pergunte_ao_chatgpt(pergunta: str):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )
    # Extracting the actual content message from the response
    return response.choices[0].message.content

# Asking the question
question = "Qual a Capital do Brasil?"
answer = pergunte_ao_chatgpt(question)

# Print the response
print(f"Resposta do ChatGpt: {answer}")
