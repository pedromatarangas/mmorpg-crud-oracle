# =====================================================================
# entrada.py
# Funções para ler o que o usuário digita SEM deixar o programa quebrar.
# Todas repetem a pergunta até o usuário digitar algo válido.
# =====================================================================
from datetime import datetime

def ler_inteiro(mensagem, minimo=None, maximo=None):
    """Lê um número inteiro. Se minimo/maximo forem informados, respeita o intervalo."""
    while True:
        texto = input(mensagem).strip()
        try:
            numero = int(texto)
        except ValueError:
            print(" Digite apenas números inteiros.")
            continue
        if minimo is not None and numero < minimo:
            print(f" O valor mínimo é {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            print(f" O valor máximo é {maximo}.")
            continue
        return numero

def ler_texto(mensagem, tamanho_maximo):
    """Lê um texto obrigatório, com limite de caracteres."""
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print(" Este campo é obrigatório.")
            continue
        if len(texto) > tamanho_maximo:
            print(f" Use no máximo {tamanho_maximo} caracteres.")
            continue
        # A aspa simples quebraria o SQL montado como texto
        if "'" in texto:
            print(" Não use aspas simples (').")
            continue
        return texto

def ler_data(mensagem):
    """Lê uma data no formato dd/mm/aaaa e devolve o texto digitado."""
    while True:
        texto = input(mensagem + " (dd/mm/aaaa): ").strip()
        try:
            datetime.strptime(texto, "%d/%m/%Y")
            return texto
        except ValueError:
            print(" Data inválida. Exemplo de data correta: 25/12/2026")

def perguntar_sim_nao(mensagem):
    """Faz uma pergunta de Sim ou Não. Devolve True para Sim e False para Não."""
    while True:
        resposta = input(mensagem + " (S/N): ").strip().upper()
        if resposta in ("S", "SIM"):
            return True
        if resposta in ("N", "NAO", "NÃO"):
            return False
        print(" Responda S ou N.")

