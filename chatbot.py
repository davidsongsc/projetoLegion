from chatbot import chatbot
from chatbot import

# Crie um chatbot
chatbot = ChatBot('Meu Chatbot')

# Crie um treinador para o chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Treine o chatbot usando o conjunto de dados de diálogo em inglês
trainer.train('chatterbot.corpus.english')

# Função para interagir com o chatbot
def chat_with_bot():
    print("Olá! Eu sou o seu chatbot. Você pode digitar 'sair' a qualquer momento para encerrar o chat.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Chatbot: Até logo!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

# Inicie a conversa
if __name__ == "__main__":
    chat_with_bot()
