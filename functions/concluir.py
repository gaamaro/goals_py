import os
import json
from datetime import datetime
from InquirerPy import prompt

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def concluir():
    clear_terminal()
    with open('database/db.json', 'r+') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        if not metas:
            print("\nNenhuma meta cadastrada.\n")
            input("\nPressione Enter para voltar ao menu principal...")
            return

        choices = [{"name": f"{meta['name']} - {meta['propriedades']['dataFim']} - {meta['propriedades']['prioridade']}", "value": index} for index, meta in enumerate(metas)]
        questions = [
            {"type": "checkbox", "name": "meta_indices", "message": "Selecione as metas para concluir:", "choices": choices}
        ]
        resposta = prompt(questions)
        metas_selecionadas = [metas[i] for i in resposta['meta_indices']]

        if not metas_selecionadas:
            print("\nNenhuma meta selecionada.\n")
            input("\nPressione Enter para voltar ao menu principal...")
            return

        confirmacao = prompt([
            {"type": "confirm", "name": "confirmar", "message": f"Você deseja concluir as seguintes metas?\n{', '.join([meta['name'] for meta in metas_selecionadas])}", "default": False}
        ])

        if confirmacao['confirmar']:
            for i in resposta['meta_indices']:
                metas[i]['propriedades']['status'] = "concluída"
                metas[i]['propriedades']['conclusao'] = datetime.now().strftime("%Y-%m-%d")

            data['metas'] = metas

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

            clear_terminal()
            print("\nMetas concluídas com sucesso!\n")
        else:
            clear_terminal()
            print("\nOperação cancelada.\n")

        input("\nPressione Enter para voltar ao menu principal...")
