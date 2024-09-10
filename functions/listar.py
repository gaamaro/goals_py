import os
import json
from tabulate import tabulate

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar():
    clear_terminal()
    with open('database/db.json', 'r') as file:
        data = json.load(file)
        metas = data.get('metas', [])

        if not metas:
            print("\nNenhuma meta cadastrada.\n")
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
        ] for meta in metas]

        print("\n" + tabulate(tabela, headers=["Finalizada", "Nome", "Data Início", "Data Fim", "Conclusão", "Prioridade", "Tags"]) + "\n")
        input("\nPressione Enter para voltar ao menu principal...")
