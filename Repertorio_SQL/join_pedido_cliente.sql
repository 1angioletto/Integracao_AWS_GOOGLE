CREATE OR REPLACE TABLE `pm_web.pm_web_resultado` AS
SELECT DISTINCT
    COD_CLIENTE,
    ID,
    COD_PEDIDO,
    CODIGO_PRODUTO,
    DEPTO,
    QUANTIDADE,
    VALOR_UNITARIO,
    QTD_PARCELAS,
    DT_PEDIDO,
    MEIO_PAGTO,
    STATUS_PAGAMENTO,
    EMAIL,
    NOME,
    DT_NASC,
    SEXO,
    CADASTRO,
    CIDADE,
    ESTADO,
    RECEBE_EMAIL
  from `pm_web.pm_web_pedidos` p
  join `pm_web.pm_web_cadastros` c on p.COD_CLIENTE = c.id
