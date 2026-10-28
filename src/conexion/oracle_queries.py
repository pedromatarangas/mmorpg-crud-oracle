# =====================================================================
# oracle_queries.py
# Classe que faz a "ponte" entre o Python e o banco Oracle.
# Todo o resto do sistema usa esta classe para mandar SQL pro banco.
# =====================================================================

import oracledb as driver

USUARIO = "labdatabase"
SENHA = "lab@Database2025" # senha usada no exemplo do professor; confira
HOST = "localhost"
PORTA = 1521
SID = ""
SERVICE_NAME = "XEPDB1"

class OracleQueries:
    
    def __init__(self):
        self.conexao = None
        self.cursor = None
    
    def conectar(self):
        """Abre a conexão com o banco, se ainda não estiver aberta."""
        if self.conexao is None:
            endereco = driver.makedsn(HOST, PORTA, service_name=SERVICE_NAME)
            self.conexao = driver.connect(user=USUARIO, password=SENHA, dsn=endereco)
            # O cursor é quem de fato executa os comandos SQL
            self.cursor = self.conexao.cursor()

    def limpar_sql(self, sql):
        """Prepara o SQL antes de enviar: tira as linhas de comentário (--),
        os espaços e o ';' do final (a biblioteca não aceita ';')."""
        linhas = [linha for linha in sql.splitlines() if not linha.strip().startswith("--")]
        return "\n".join(linhas).strip().rstrip(";")

    def consultar(self, sql):
        """Executa um SELECT e devolve uma lista de linhas.
        Cada linha é uma tupla, ex.: [(1, 'Lobos de Prata'), (2, 'Ordem do Dragao')]"""
        self.conectar()
        self.cursor.execute(self.limpar_sql(sql))
        return self.cursor.fetchall()
    
    def executar(self, sql):
        """Executa INSERT, UPDATE ou DELETE e salva (commit).
        Devolve True se deu certo e False se o banco recusou."""
        self.conectar()
        try:
            self.cursor.execute(self.limpar_sql(sql))
            self.conexao.commit()
            return True
        except driver.DatabaseError as erro:
            self.conexao.rollback()
            print(f"\n [ERRO DO BANCO] {erro}")
            return False
    
    def proximo_id(self, nome_sequence):
        """Pede o próximo número de uma sequence, ex.: GUILDAS_ID_SEQ."""
        linhas = self.consultar(f"select {nome_sequence}.nextval from dual")
        return int(linhas[0][0])
    
    def imprimir(self, sql):
        """Executa um SELECT e mostra o resultado como tabela na tela.
        Devolve quantas linhas foram mostradas."""
        self.conectar()
        self.cursor.execute(self.limpar_sql(sql))
        # Nomes das colunas, na ordem do SELECT
        colunas = [descricao[0] for descricao in self.cursor.description]
        linhas = self.cursor.fetchall()
        
        if len(linhas) == 0:
            print(" (nenhum registro encontrado)")
            return 0

        # Calcula a largura de cada coluna (o maior texto dela)
        larguras = [len(nome) for nome in colunas]
        for linha in linhas:
            for i in range(len(linha)):
                larguras[i] = max(larguras[i], len(self.texto(linha[i])))

        # Cabeçalho, linha separadora e as linhas de dados
        cabecalho = " | ".join(colunas[i].ljust(larguras[i]) for i in range(len(colunas)))
        print(" " + cabecalho)
        print(" " + "-+-".join("-" * largura for largura in larguras))
        for linha in linhas:
            print(" " + " | ".join(self.texto(linha[i]).ljust(larguras[i]) for i in range(len(linha))))
        return len(linhas)

    def texto(self, valor):
        """Transforma um valor vindo do banco em texto (None vira vazio)."""
        if valor is None:
            return ""
        return str(valor)
    
    def fechar(self):
        """Fecha a conexão com o banco."""
        if self.conexao is not None:
            self.conexao.close()
            self.conexao = None
            self.cursor = None