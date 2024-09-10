import os
import typer
from InquirerPy import prompt
from functions import cadastrar, deletar, listar, metas_abertas, metas_realizadas, concluir

app = typer.Typer()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        while True:
            clear_terminal()
            menu = [
                {
                    "type": "list",
                    "name": "action",
                    "message": "Goals Py\nMenu principal:",
                    "choices": [
                        "Cadastrar meta",
                        "Listar metas",
                        "Metas realizadas",
                        "Metas abertas",
                        "Concluir metas",
                        "Deletar metas",
                        "Sair"
                    ]
                }
            ]
            resposta = prompt(menu)
            action = resposta["action"]

            if action == "Cadastrar meta":
                cadastrar()
            elif action == "Listar metas":
                listar()
            elif action == "Metas realizadas":
                metas_realizadas()
            elif action == "Metas abertas":
                metas_abertas()
            elif action == "Concluir metas":
                concluir()
            elif action == "Deletar metas":
                deletar()
            elif action == "Sair":
                break

    except KeyboardInterrupt:
        print("\nSaindo...")
        os._exit(0)

    except Exception as e:
        print(f"Erro: {e}") 

    finally:
        os._exit(0)

if __name__ == "__main__":
    main()
