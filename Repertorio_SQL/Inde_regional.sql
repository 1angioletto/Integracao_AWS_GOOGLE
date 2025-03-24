SELECT 
    ESTADO      
  ,DEPTO         as Departamento
  ,count(DEPTO)  as Qtd_dep
  ,ROUND(sum(VALOR_UNITARIO * QUANTIDADE), 2) as Valor
FROM 
    pm_web.pm_web_resultado
WHERE ESTADO is not null

GROUP BY 1,2
ORDER BY Qtd_dep DESC
