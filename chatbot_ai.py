#instalando a ia do google
!pip install google-generativeai

#importando a ia do google
import google.generativeai as ai
import os

# Chave API 
API_KEY = 'put your secret key here!'

import google.generativeai as genai

API_KEY = 'Put yout secret key here!'

# 1. Configura a API (certifique-se de ter a chave configurada no seu ambiente)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
ai.configure(api_key=API_KEY)

# 2. Inicializa o modelo (ex: gemini-1.5-flash)
model = ai.GenerativeModel('gemini-2.5-flash')

# 3. Cria o objeto de chat. Ele gerencia o histórico automaticamente!
chat = model.start_chat(history=[])

print("Chatbot iniciado! Digite 'bye' para sair.\n")

# Inicia a conversa
while True:
    mensagem = input('Você: ')
    if mensagem.lower() == 'bye':
        print('Chatbot: Até a próxima!')
        break
    
    try:
        # Envia APENAS a nova mensagem. O objeto 'chat' anexa o histórico por debaixo dos panos.
        resposta = chat.send_message(mensagem)
        
        # Exibe a resposta da IA
        print(f"Chatbot: {resposta.text}\n")
        
    except Exception as e:
        print(f"\n[Erro ao se comunicar com a API]: {e}")
        break

#Se em algum momento você precisar visualizar ou exportar o histórico que
# o chat guardou automaticamente, você pode acessá-lo a qualquer momento usando:

for message in chat.history:
    print(f"{message.role}: {message.parts[0].text}")


#Abaixo o código para obter o modelo mais atualizado do Gemini
'''

# Configura a API
ai.configure(api_key=API_KEY)

# Lista todos os modelos disponíveis e suas capacidades
for model in genai.list_models():
    print(f"Nome: {model.name}")
    print(f"Descrição: {model.description}")
    print(f"Métodos suportados: {model.supported_generation_methods}\n")
'''
