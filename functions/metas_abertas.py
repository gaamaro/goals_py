import json
from tabulate import tabulate

def metas_abertas():
    with open('database/db.json', 'r') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        metas_abertas = [meta for meta in metas if meta['propriedades']['status'] == "aberta"]

        if not metas_abertas:
            print("\nNenhuma meta aberta.\n")
            return

        tabela = [[
            "✔️" if meta['propriedades']['status'] == "concluída" else "❌",
            meta['name'],
            meta['propriedades'].get('dataInicio', ''),
            meta['propriedades'].get('dataFim', ''),
            meta['propriedades'].get('conclusao', ''),
            meta['propriedades'].get('prioridade', ''),
            ', '.join(meta['propriedades'].get('tags', []))
        ] for meta in metas_abertas]

        print("\n" + tabulate(tabela, headers=["Finalizada", "Nome", "Data Início", "Data Fim", "Conclusão", "Prioridade", "Tags"]) + "\n")
