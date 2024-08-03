# O uso da api groq pode ser substituído pela api local sem grandes problemas apenas descomentando o código abaixo e apagando o posterior.

# from ollama import chat

# def generate_code(documento, pergunta):
#     response = chat(
#         model='llama3',
#         messages=[
#             {
#                 "role": "user",
#             "content": f""" Responda às perguntas com base no documento abaixo:
#                         Documento:
#                         ------
#                         {documento}
#                         ------

#                         Pergunta:
#                         --------
#                         {pergunta}
#                         --------
#                         """,
#             },
#         ],
#     )
#     return response['message']['content'].replace('`', '')

from groq import Groq

client = Groq(
    api_key="SUA_CHAVE", # chave da api do groq
)


def generate_code(documento, pergunta):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f""" Responda às perguntas com base no documento abaixo:
                        Documento:
                        ------
                        {documento}
                        ------

                        Pergunta:
                        --------
                        {pergunta}
                        --------
                        """,
        }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content