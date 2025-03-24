SELECT 
    ID,
    DEPTO,
    CONCAT(FORMAT_DATE('%B', PARSE_DATE('%d/%m/%Y', DT_PEDIDO)), ' ', EXTRACT(YEAR FROM PARSE_DATE('%d/%m/%Y', DT_PEDIDO))) AS MES_ANO,
    SUM(QUANTIDADE) AS QUANTIDADE,
    SUM(VALOR_UNITARIO * QUANTIDADE) AS VALOR_TOTAL,
    CASE 
        WHEN SUM(VALOR_UNITARIO * QUANTIDADE) <= 1000 THEN 'Básico'
        WHEN SUM(VALOR_UNITARIO * QUANTIDADE) > 1000 AND SUM(VALOR_UNITARIO * QUANTIDADE) <= 2000 THEN 'Prata'
        WHEN SUM(VALOR_UNITARIO * QUANTIDADE) > 2000 AND SUM(VALOR_UNITARIO * QUANTIDADE) <= 5000 THEN 'Ouro'
        WHEN SUM(VALOR_UNITARIO * QUANTIDADE) > 5000 THEN 'Super'
    END AS FAIXA
FROM 
    pm_web.pm_web_resultado
GROUP BY 
    ID,DEPTO,MES_ANO
ORDER BY 
    Valor_total DESC;
