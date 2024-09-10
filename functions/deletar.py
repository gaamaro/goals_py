import os
import json
from InquirerPy import prompt

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def deletar():
    clear_terminal()
    with open('database/db.json', 'r+') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        if not metas:
            print("Nenhuma meta cadastrada.")
            input("\nPressione Enter para voltar ao menu principal...")
            return

        choices = [{"name": f"{meta['name']} - {meta['propriedades']['dataFim']} - {meta['propriedades']['prioridade']}", "value": index} for index, meta in enumerate(metas)]
        questions = [{"type": "list", "name": "meta_index", "message": "Selecione a meta para deletar:", "choices": choices}]
        resposta = prompt(questions)

        clear_terminal()
        confirmacao = prompt([
            {"type": "confirm", "name": "confirmar", "message": f"Você deseja deletar a seguinte meta?\n{metas[resposta['meta_index']]}", "default": False}
        ])

        if confirmacao['confirmar']:
            metas.pop(resposta['meta_index'])
            data['metas'] = metas

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

            clear_terminal()
            print("Meta deletada com sucesso!")
        else:
            clear_terminal()
            print("Operação cancelada.")

        input("\nPressione Enter para voltar ao menu principal...")
