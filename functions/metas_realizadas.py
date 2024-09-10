import json
from tabulate import tabulate

def metas_realizadas():
    with open('database/db.json', 'r') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        metas_realizadas = [meta for meta in metas if meta['propriedades']['status'] == "concluída"]

        if not metas_realizadas:
            print("\nNenhuma meta realizada.\n")
            return

        tabela = [[
            "✔️" if meta['propriedades']['status'] == "concluída" else "❌",
            meta['name'],
            meta['propriedades'].get('dataInicio', ''),
            meta['propriedades'].get('dataFim', ''),
            meta['propriedades'].get('conclusao', ''),
            meta['propriedades'].get('prioridade', ''),
            ', '.join(meta['propriedades'].get('tags', []))
        ] for meta in metas_realizadas]

        print("\n" + tabulate(tabela, headers=["Finalizada", "Nome", "Data Início", "Data Fim", "Conclusão", "Prioridade", "Tags"]) + "\n")
