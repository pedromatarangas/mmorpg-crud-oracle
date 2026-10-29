-- Relatório de SUMARIZAÇÃO (GROUP BY): personagens agrupados por classe
select p.classe as classe
     , count(1) as qtd_personagens
     , round(avg(p.nivel), 1) as nivel_medio
     , max(p.nivel) as maior_nivel
from personagens p
group by p.classe
order by p.classe
