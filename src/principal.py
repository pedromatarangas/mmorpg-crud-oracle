# =====================================================================
# principal.py
# Ponto de partida do sistema: mostra a splash screen e o menu
# principal, e chama os relatórios e os controllers.
# Para executar (de dentro da pasta src):  python3 principal.py
# =====================================================================
from utils import config
from utils.entrada import ler_inteiro
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_guilda import Controller_Guilda
from controller.controller_jogador import Controller_Jogador
from controller.controller_personagem import Controller_Personagem

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_guilda = Controller_Guilda()
ctrl_jogador = Controller_Jogador()
ctrl_personagem = Controller_Personagem()


def menu_relatorios():
    while True:
        config.limpar_tela()
        print(config.MENU_RELATORIOS)
        opcao = ler_inteiro("Escolha uma opção [0-3]: ", 0, 3)
        if opcao == 0:
            break
        elif opcao == 1:
            relatorio.get_relatorio_personagens_por_classe()
        elif opcao == 2:
            relatorio.get_relatorio_personagens_por_guilda()
        elif opcao == 3:
            relatorio.get_relatorio_personagens_completo()


def escolher_entidade(acao):
    """Mostra o menu de tabelas e devolve a opção (0 = voltar)."""
    config.limpar_tela()
    print(f"\n========== {acao} ==========")
    print(config.MENU_ENTIDADES)
    return ler_inteiro("Escolha uma opção [0-3]: ", 0, 3)


def inserir():
    opcao = escolher_entidade("INSERIR REGISTROS")
    if opcao == 1:
        ctrl_guilda.inserir_guilda()
    elif opcao == 2:
        ctrl_jogador.inserir_jogador()
    elif opcao == 3:
        ctrl_personagem.inserir_personagem()


def atualizar():
    opcao = escolher_entidade("ATUALIZAR REGISTROS")
    if opcao == 1:
        ctrl_guilda.atualizar_guilda()
    elif opcao == 2:
        ctrl_jogador.atualizar_jogador()
    elif opcao == 3:
        ctrl_personagem.atualizar_personagem()


def remover():
    opcao = escolher_entidade("REMOVER REGISTROS")
    if opcao == 1:
        ctrl_guilda.excluir_guilda()
    elif opcao == 2:
        ctrl_jogador.excluir_jogador()
    elif opcao == 3:
        ctrl_personagem.excluir_personagem()


def run():
    config.limpar_tela()
    print(tela_inicial.gerar_tela())
    config.pausar()

    while True:
        config.limpar_tela()
        print(config.MENU_PRINCIPAL)
        opcao = ler_inteiro("Escolha uma opção [1-5]: ", 1, 5)

        if opcao == 1:
            menu_relatorios()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            remover()
        elif opcao == 5:
            config.limpar_tela()
            print(tela_inicial.gerar_tela())
            print("\nObrigado por utilizar o nosso sistema!")
            break


if __name__ == "__main__":
    try:
        run()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C (ou Ctrl+D): encerra sem mostrar mensagem de erro
        print("\n\nPrograma encerrado.")