import os
from conexion.oracle_queries import OracleQueries
from utils import config


PASTA_SQL = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sql")


class Relatorio:
    def __init__(self):
        self.query_por_classe = self.ler_arquivo("relatorio_personagens_por_classe.sql")
        self.query_por_guilda = self.ler_arquivo("relatorio_personagens_por_guilda.sql")
        self.query_completo = self.ler_arquivo("relatorio_personagens_completo.sql")

    def ler_arquivo(self, nome_arquivo):
        """Abre um arquivo da pasta src/sql e devolve o texto dele."""
        caminho = os.path.join(PASTA_SQL, nome_arquivo)
        with open(caminho, encoding="utf-8") as arquivo:
            return arquivo.read()

    def mostrar(self, titulo, query):
        """Mostra o título, executa a consulta e espera o Enter."""
        print(f"\n=== {titulo} ===\n")
        oracle = OracleQueries()
        oracle.imprimir(query)
        oracle.fechar()
        config.pausar()

    def get_relatorio_personagens_por_classe(self):
        self.mostrar("PERSONAGENS POR CLASSE", self.query_por_classe)

    def get_relatorio_personagens_por_guilda(self):
        self.mostrar("PERSONAGENS POR GUILDA", self.query_por_guilda)

    def get_relatorio_personagens_completo(self):
        self.mostrar("LISTA COMPLETA DE PERSONAGENS", self.query_completo)
