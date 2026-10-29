-- Relatório de SUMARIZAÇÃO com JUNÇÃO: membros e nível médio de cada guilda
-- (LEFT JOIN para mostrar também as guildas que ainda não têm personagens)
select g.nome as guilda
     , count(p.id_personagem) as qtd_membros
     , nvl(round(avg(p.nivel), 1), 0) as nivel_medio
from guildas g
left join personagens p
       on p.id_guilda = g.id_guilda
group by g.nome
order by qtd_membros desc, g.nome
