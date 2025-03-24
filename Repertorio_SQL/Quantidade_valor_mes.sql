select DEPTO
      ,SUM(QUANTIDADE) as Quantidade
      ,ROUND(SUM(VALOR_UNITARIO * QUANTIDADE), 2) AS VALOR_TOTAL_VENDAS
      ,FORMAT_DATE('%B', PARSE_DATE('%d/%m/%Y', DT_PEDIDO)) AS MES
 from pm_web.pm_web_resultado
 group by DEPTO, MES
 order by vaLOR_TOTAL_VENDAS desc
