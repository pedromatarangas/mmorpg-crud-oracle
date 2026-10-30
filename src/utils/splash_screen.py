# =====================================================================
# splash_screen.py
# Monta a tela inicial: título em ASCII art, total de registros de cada
# tabela, integrantes, disciplina, semestre e professor.
# =====================================================================
from conexion.oracle_queries import OracleQueries
from utils import config

# Códigos de cor do terminal (o RESET volta para a cor normal)
AMARELO = "\033[93m"
CIANO = "\033[96m"
VERDE = "\033[92m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

# Título em letras grandes. O "r" antes das aspas faz o Python
# não interpretar as barras invertidas (\) como comandos especiais.
TITULO_ASCII = r"""
 __  __ __  __  ___  ____  ____   ____
|  \/  |  \/  |/ _ \|  _ \|  _ \ / ___|
| |\/| | |\/| | | | | |_) | |_) | |  _
| |  | | |  | | |_| |  _ <|  __/| |_| |
|_|  |_|_|  |_|\___/|_| \_\_|    \____|
"""


class SplashScreen:

    def __init__(self):
        self.largura = 56   # largura interna do quadro (sem as bordas)

    def linha(self, texto="", cor=""):
        """Monta uma linha do quadro: ║ texto ║.
        O espaçamento é calculado ANTES de colocar a cor, para a cor
        não atrapalhar o alinhamento da borda da direita."""
        texto_alinhado = (" " + texto).ljust(self.largura)
        return "║" + cor + texto_alinhado + RESET + "║"

    def centralizada(self, texto, cor=""):
        """Monta uma linha do quadro com o texto no centro."""
        return "║" + cor + texto.center(self.largura) + RESET + "║"

    def contar_registros(self, oracle, tabela):
        """Executa o select count da tabela e devolve o número."""
        sql = config.QUERY_COUNT.format(tabela=tabela)
        return oracle.consultar(sql)[0][0]

    def gerar_tela(self):
        """Devolve o texto completo da splash screen."""
        oracle = OracleQueries()
        topo = "╔" + "═" * self.largura + "╗"
        divisao = "╠" + "═" * self.largura + "╣"
        base = "╚" + "═" * self.largura + "╝"

        linhas = [topo]

        # Título em ASCII art, centralizado e em amarelo
        for parte in TITULO_ASCII.strip("\n").split("\n"):
            linhas.append(self.centralizada(parte.ljust(39), AMARELO + NEGRITO))
        linhas.append(self.centralizada(config.NOME_SISTEMA, NEGRITO))
        linhas.append(divisao)

        # Contagem de registros de cada tabela
        linhas.append(self.linha("TOTAL DE REGISTROS EXISTENTES", NEGRITO))
        numero = 1
        for tabela in config.TABELAS:
            total = self.contar_registros(oracle, tabela)
            linhas.append(self.linha(f"   {numero} - {tabela + ':':<14}{total:>6}", CIANO))
            numero = numero + 1
        linhas.append(divisao)

        # Integrantes do grupo
        linhas.append(self.linha("CRIADO POR: " + config.INTEGRANTES[0], VERDE))
        for nome in config.INTEGRANTES[1:]:
            linhas.append(self.linha("            " + nome, VERDE))
        linhas.append(divisao)

        # Disciplina, semestre e professor
        linhas.append(self.linha("DISCIPLINA: " + config.DISCIPLINA))
        linhas.append(self.linha("            " + config.SEMESTRE))
        linhas.append(self.linha("PROFESSOR:  " + config.PROFESSOR))
        linhas.append(base)

        oracle.fechar()
        return "\n".join(linhas)