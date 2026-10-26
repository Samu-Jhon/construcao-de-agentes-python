
from pathlib import Path
import shutil

# Localiza a pasta ArquivosGerais dentro de Downloads
pasta_geral = Path.home() / "Downloads" / "ArquivosGerais"

# Verifica se a pasta existe
if not pasta_geral.is_dir():
    print("ERRO: Pasta ArquivosGerais nao encontrada!")
    print("Caminho esperado:", pasta_geral)

else:
    print("=== ORGANIZADOR AUTOMATICO DE ARQUIVOS ===")

    # Percorre os arquivos da pasta
    quantidade = 0

    for arquivo in pasta_geral.iterdir():

        # Ignora pastas e seleciona apenas arquivos
        if arquivo.is_file():

            # Identifica a extensao do arquivo
            extensao = arquivo.suffix.replace(".", "").upper()

            # Arquivos sem extensao
            if extensao == "":
                extensao = "SEM_EXTENSAO"

            # Define e cria a pasta de destino
            pasta_destino = pasta_geral / extensao
            pasta_destino.mkdir(exist_ok=True)

            # Define o caminho final do arquivo
            destino = pasta_destino / arquivo.name

            # Evita substituir arquivos com nomes iguais
            contador = 1

            while destino.exists():
                novo_nome = (
                    f"{arquivo.stem}_{contador}{arquivo.suffix}"
                )
                destino = pasta_destino / novo_nome
                contador += 1

            # Move o arquivo para sua pasta
            try:
                shutil.move(str(arquivo), str(destino))
                quantidade += 1

                print(f"Organizado: {arquivo.name} -> {extensao}")

            except OSError as erro:
                print(f"Erro ao mover {arquivo.name}: {erro}")

    print("\n=== ORGANIZACAO FINALIZADA ===")
    print(f"Total de arquivos organizados: {quantidade}")
