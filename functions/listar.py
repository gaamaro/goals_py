import json
from tabulate import tabulate

def listar():
    with open('database/db.json', 'r') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        if not metas:
            print("\nNenhuma meta cadastrada.\n")
            return

        tabela = [[
            "✔️" if meta['propriedades']['status'] == "concluída" else "❌",
            meta['name'],
            meta['propriedades'].get('dataInicio', ''),
            meta['propriedades'].get('dataFim', ''),
            meta['propriedades'].get('conclusao', ''),
            meta['propriedades'].get('prioridade', ''),
            ', '.join(meta['propriedades'].get('tags', []))
        ] for meta in metas]

        print("\n" + tabulate(tabela, headers=["Finalizada", "Nome", "Data Início", "Data Fim", "Conclusão", "Prioridade", "Tags"]) + "\n")
