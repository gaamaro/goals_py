import os
import json
from datetime import datetime
from InquirerPy import prompt

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar():
    clear_terminal()
    with open('database/db.json', 'r+') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        current_year = datetime.now().year
        current_month = f"{datetime.now().month:02d}"
        current_day = f"{datetime.now().day:02d}"
        years = [str(year) for year in range(current_year, current_year + 11)]
        months = [f"{month:02d}" for month in range(1, 13)]
        days = [f"{day:02d}" for day in range(1, 32)]

        # Coletar todas as tags existentes
        existing_tags = set()
        for meta in metas:
            existing_tags.update(meta['propriedades'].get('tags', []))
        existing_tags = list(existing_tags)

        questions = [
            {"type": "input", "name": "name", "message": "Nome da meta:"},
            {"type": "list", "name": "year", "message": "Ano de término:", "choices": years, "default": str(current_year)},
            {"type": "list", "name": "month", "message": "Mês de término:", "choices": months, "default": current_month},
            {"type": "list", "name": "day", "message": "Dia de término:", "choices": days, "default": current_day},
            {"type": "list", "name": "prioridade", "message": "Prioridade:", "choices": ["Alta", "Média", "Baixa"], "default": "Média"},
            {"type": "checkbox", "name": "existing_tags", "message": "Selecione as tags existentes:", "choices": existing_tags},
            {"type": "input", "name": "new_tags", "message": "Adicione novas tags (separadas por vírgula):"}
        ]

        resposta = prompt(questions)
        data_fim = f"{resposta.pop('year')}-{resposta.pop('month')}-{resposta.pop('day')}"
        existing_tags = resposta.pop('existing_tags')
        new_tags = [tag.strip() for tag in resposta.pop('new_tags').split(',')] if resposta['new_tags'] else []
        tags = existing_tags + new_tags

        resposta['propriedades'] = {
            "dataFim": data_fim,
            "dataInicio": datetime.now().strftime("%Y-%m-%d"),
            "status": "aberta",
            "conclusao": "",
            "prioridade": resposta.pop('prioridade').lower(),
            "tags": tags
        }

        clear_terminal()
        confirmacao = prompt([
            {"type": "confirm", "name": "confirmar", "message": f"Você deseja cadastrar a seguinte meta?\n{resposta}", "default": True}
        ])

        if confirmacao['confirmar']:
            metas.append(resposta)
            data['metas'] = metas

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

            clear_terminal()
            print("Meta cadastrada com sucesso!")
        else:
            clear_terminal()
            print("Operação cancelada.")

        input("\nPressione Enter para voltar ao menu principal...")