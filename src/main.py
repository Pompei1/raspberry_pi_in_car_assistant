def main():
    print("Assistente veicular iniciado.")

if __name__ == "__main__":
    main()

from core.assistant import Assistant

def main():
    assistant = Assistant()
    
    while True:
        command = input("Digite um comando: ")
        response = assistant.process(command)
        print(response)

if __name__ == "__main__":
    main()
