SELECT 
    t1.DEPTO,
    COALESCE(t1.Valor_2019, 0) AS Valor_2019,
    COALESCE(t2.Valor_2020, 0) AS Valor_2020,
    CASE
        WHEN t1.Valor_2019 = 0 THEN NULL  -- Evitar divisão por 0
        ELSE ((t2.Valor_2020 - t1.Valor_2019) ) * 100 
    END AS Diferenca_Porcentual
FROM 
    (SELECT 
        DEPTO,
        SUM(VALOR_UNITARIO * QUANTIDADE) AS Valor_2019
     FROM 
        pm_web.pm_web_resultado
     WHERE 
        DT_PEDIDO BETWEEN '01/01/2019' AND '31/12/2019'
        AND DEPTO IN ('SOM', 'PAPELARIA')
     GROUP BY 
        DEPTO) t1
LEFT JOIN 
    (SELECT 
        DEPTO,
        SUM(VALOR_UNITARIO * QUANTIDADE) AS Valor_2020
     FROM 
        pm_web.pm_web_resultado
     WHERE 
        DT_PEDIDO BETWEEN '01/01/2020' AND '31/12/2020'
        AND DEPTO IN ('SOM', 'PAPELARIA')
     GROUP BY 
        DEPTO) t2
ON t1.DEPTO = t2.DEPTO;
