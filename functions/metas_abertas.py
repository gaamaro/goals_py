import os
import json
from tabulate import tabulate

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def metas_abertas():
    clear_terminal()
    with open('database/db.json', 'r') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        metas_abertas = [meta for meta in metas if meta['propriedades']['status'] == "aberta"]

        if not metas_abertas:
            print("\nNenhuma meta aberta.\n")
            input("\nPressione Enter para voltar ao menu principal...")
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
        input("\nPressione Enter para voltar ao menu principal...")
