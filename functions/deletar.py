import json
from InquirerPy import prompt

def deletar():
    with open('database/db.json', 'r+') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        if not metas:
            print("Nenhuma meta cadastrada.")
            return

        choices = [{"name": f"{meta['name']} - {meta['propriedades']['dataFim']} - {meta['propriedades']['prioridade']}", "value": index} for index, meta in enumerate(metas)]
        questions = [{"type": "list", "name": "meta_index", "message": "Selecione a meta para deletar:", "choices": choices}]
        resposta = prompt(questions)

        metas.pop(resposta['meta_index'])
        data['metas'] = metas

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print("Meta deletada com sucesso!")
