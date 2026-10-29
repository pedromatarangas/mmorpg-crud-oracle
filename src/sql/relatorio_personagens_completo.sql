-- Relatório de JUNÇÃO (JOIN): cada personagem com o nickname do dono e o nome da guilda
select p.id_personagem as id
     , p.nome as personagem
     , p.classe as classe
     , p.nivel as nivel
     , j.nickname as jogador
     , g.nome as guilda
from personagens p
inner join jogadores j
        on j.id_jogador = p.id_jogador
inner join guildas g
        on g.id_guilda = p.id_guilda
order by g.nome, p.nivel desc
