# Roteiro do vídeo — Sistema de Gerenciamento de MMORPG

Duração: uns 5 a 8 minutos. Gravar a tela da VM (OBS Studio) com microfone ligado.
Publicar no YouTube como **Não listado** e mandar o link para o Pedro colocar no README.

| # | Parte | Tempo | O que mostrar / falar |
|---|-------|-------|-----------------------|
| 1 | Abertura | 30 s | Nomes do grupo e objetivo: "sistema de gerenciamento de um MMORPG, com jogadores, guildas e personagens, em Python com banco Oracle". |
| 2 | Diagrama | 30 s | Mostrar `diagrams/diagrama_relacional.png` e explicar as 3 tabelas e as ligações (um jogador tem vários personagens; uma guilda tem vários personagens). |
| 3 | Splash screen | 20 s | Rodar `python3 principal.py` e mostrar os totais de cada tabela e os nomes do grupo. |
| 4 | Relatórios | 1 min | Abrir os 3 relatórios: por classe (group by), por guilda (group by + left join) e lista completa (join). |
| 5 | Inserir | 1 min 30 s | Inserir uma guilda, um jogador e um personagem nessa guilda e desse jogador. Mostrar um erro tratado (ex.: data inválida) e o "Deseja inserir mais?". |
| 6 | Atualizar | 1 min | Atualizar o personagem criado e mostrar o registro atualizado. |
| 7 | Remover | 1 min 30 s | Remover uma guilda que tem personagens: mostrar o aviso, responder **N**, repetir e responder **S**. Remover um personagem. |
| 8 | Fechamento | 20 s | Sair pelo menu (opção 5) e mostrar a splash com os totais atualizados. |

## Observações
- Gravação com o grupo no dia 30, depois que o Pedro juntar tudo.
- Não precisa explicar código, só o objetivo e o sistema funcionando em todos os menus.
