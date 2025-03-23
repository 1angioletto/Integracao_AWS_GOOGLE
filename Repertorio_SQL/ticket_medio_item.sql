select DEPTO
      ,SUM(QUANTIDADE) as Quantidade
      ,ROUND(avg(VALOR_UNITARIO/QUANTIDADE), 2) AS ticket_Medio

 from pm_web.pm_web_resultado
 group by DEPTO
 order by Quantidade desc
