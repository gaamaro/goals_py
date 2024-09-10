import json
from datetime import datetime
from InquirerPy import prompt

def cadastrar():
    with open('database/db.json', 'r+') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        questions = [
            {"type": "input", "name": "name", "message": "Nome da meta:"},
            {"type": "input", "name": "dataFim", "message": "Data de término (YYYY-MM-DD):"},
            {"type": "list", "name": "prioridade", "message": "Prioridade:", "choices": ["Alta", "Média", "Baixa"]},
            {"type": "input", "name": "tags", "message": "Tags (separadas por vírgula):"}
        ]

        resposta = prompt(questions)
        resposta['propriedades'] = {
            "dataFim": resposta.pop('dataFim'),
            "dataInicio": datetime.now().strftime("%Y-%m-%d"),
            "status": "aberta",
            "conclusao": "",
            "prioridade": resposta.pop('prioridade').lower(),
            "tags": [tag.strip() for tag in resposta.pop('tags').split(',')]
        }

        metas.append(resposta)
        data['metas'] = metas

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print("Meta cadastrada com sucesso!")
