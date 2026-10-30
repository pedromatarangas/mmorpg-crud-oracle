# =====================================================================
# criar_tabelas.py
# Apaga e recria todas as tabelas, executando os scripts da pasta sql
# na ordem certa, e insere os dados de exemplo.
# Para executar (de dentro da pasta src):  python3 criar_tabelas.py
# =====================================================================
import os
from conexion.oracle_queries import OracleQueries

# Pasta sql que fica na raiz do projeto (um nível acima de src)
PASTA_SQL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sql")

# A ordem importa: primeiro apaga tudo, depois as tabelas "mãe"
# (guildas e jogadores) e por último a "filha" (personagens)
ARQUIVOS = ["00_apagar_tudo.sql", "01_guildas.sql", "02_jogadores.sql", "03_personagens.sql"]


def ler_comandos(caminho):
    """Lê um arquivo .sql, tira os comentários e separa os comandos pelo ';'."""
    with open(caminho, encoding="utf-8") as arquivo:
        linhas = arquivo.read().splitlines()
    linhas_sem_comentario = [linha for linha in linhas if not linha.strip().startswith("--")]
    texto = "\n".join(linhas_sem_comentario)
    return [comando.strip() for comando in texto.split(";") if comando.strip() != ""]


def main():
    oracle = OracleQueries()
    oracle.conectar()

    for nome_arquivo in ARQUIVOS:
        print(f"Executando {nome_arquivo}...")
        for comando in ler_comandos(os.path.join(PASTA_SQL, nome_arquivo)):
            if comando.upper() == "COMMIT":
                oracle.conexao.commit()
                continue
            try:
                oracle.cursor.execute(comando)
            except Exception as erro:
                # No 00_apagar_tudo é normal dar erro se a tabela não existia
                if not nome_arquivo.startswith("00"):
                    print(f"  ERRO: {erro}")
                    print(f"  Comando: {comando[:70]}...")
        oracle.conexao.commit()

    oracle.fechar()
    print("\nTabelas criadas e dados de exemplo inseridos!")


if __name__ == "__main__":
    main()
