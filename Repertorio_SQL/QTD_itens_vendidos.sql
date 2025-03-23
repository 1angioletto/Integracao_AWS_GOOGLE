select DEPTO
      ,SUM(QUANTIDADE) as Quantidade
      ,ROUND(SUM(VALOR_UNITARIO * QUANTIDADE), 2) AS TOTAL_VENDAS

 from pm_web.pm_web_resultado
 group by DEPTO
