def main():
    print("Assistente veicular iniciado.")

if __name__ == "__main__":
    main()

from core.assistant import Assistant

def main():
    assistant = Assistant()
    command = input("Digite um comando: ")
    response = assistant.respond(command)
    print(response)

if __name__ == "__main__":
    main()
