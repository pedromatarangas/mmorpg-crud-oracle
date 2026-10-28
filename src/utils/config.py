# =====================================================================
# config.py
# Textos dos menus, dados da splash screen e funções de tela.
# =====================================================================
import os
NOME_SISTEMA = "SISTEMA DE GERENCIAMENTO DE MMORPG"
INTEGRANTES = [
    "PEDRO MARQUES MATARANGAS",
    "DAVI DE BRITO TEIXEIRA",
    "SAMUEL FLORIANO OLIVEIRA DE SIQUEIRA",
    "ARTUR CARMO DOS SANTOS",
    "GABRIEL LEAL HOFFOMAN",
]

DISCIPLINA = "BANCO DE DADOS"
SEMESTRE = "2026/2"
PROFESSOR = "HOWARD ROATTI"

# Tabelas que aparecem na contagem da splash screen
TABELAS = ["GUILDAS", "JOGADORES", "PERSONAGENS"]

# Consulta de contagem pedida no edital (o {tabela} é trocado pelo nome)
QUERY_COUNT = "select count(1) as total_{tabela} from {tabela}"

MENU_PRINCIPAL = """
=========== MENU PRINCIPAL ===========
  1 - Relatórios
  2 - Inserir registros
  3 - Atualizar registros
  4 - Remover registros
  5 - Sair
======================================"""

MENU_RELATORIOS = """
============== RELATÓRIOS ==============
  1 - Personagens por classe
  2 - Personagens por guilda
  3 - Lista completa de personagens
  0 - Voltar ao menu principal
========================================"""

MENU_ENTIDADES = """
  1 - Guildas
  2 - Jogadores
  3 - Personagens
  0 - Voltar ao menu principal"""

def limpar_tela():
    """Limpa o terminal."""
    os.system("clear")

def pausar():
    """Espera o usuário apertar Enter."""
    input("\nPressione Enter para continuar...")