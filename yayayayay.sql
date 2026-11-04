create database banco_exemplo_dml2922;

use banco_exemplo_dml2922;

-- safe update mode" bloqueia UPDATE/DELETE
set sql_safe_updates =0;

-- cliente da loja
create table clientes (
	id int auto_increment primary key,
	nome varchar(100),
    email varchar(100),
    cidade varchar(100),
    estado char(2),
    data_cadastro date
);

-- produtos vendidos
create table produtos (
	id int auto_increment primary key,
    nome varchar(100),
    categoria varchar(50),
    preco decimal(10,2),
    estoque int
);

-- pedidos feitos pelos clientes
create table pedidos (
	id int auto_increment primary key,
    cliente_id int,
    data_pedido date,
    status varchar(20),
    foreign key (cliente_id) references clientes(id)
);

-- itens de cada pedido (1 pedi pode ter var prod)
create table itens_pedidos(
	id int auto_increment primary key, 
    pedido_id int,
    produto_id int,
    quantidade int,
    preco_unitario decimal(10,2), -- preço no momento da venda
    foreign key (pedido_id) references pedidos(id),
    foreign key (produto_id) references produtos(id)
);

#1. INSERT - inserindo dados
insert into clientes (nome, email, cidade, estado, data_cadastro)
values ('Carlos Silva', 'carlos@email.com', 'são paulo', 'SP', '2025-01-15');

insert into clientes (nome, email, cidade, estado, data_cadastro)
values ('Ana Souza', null, 'curitiba', 'PR', '2025-02-20');

insert into produtos (nome, categoria, preco, estoque)
values ('Notebook', 'Informatica', 3500.00, 10),
		('Cadeira gamer', 'Moveis', 1200.00, 5);
        
insert into pedidos (cliente_id, data_pedido, status)
values (1, '2025-07-01', 'Enviado'),
		(1, '2025-09-02', 'pendente');
        
insert into itens_pedidos (pedido_id, produto_id, quantidade, preco_unitario)
values (1, 1, 1, 3500.00),
		(2, 2, 2, 1200.00);
        
select * from pedidos;

#2. SELECT - consultas básicas

-- 2.1 Todas colunas
select * from clientes;

-- 2.2 apenas colunas especificcas
select nome, cidade from clientes;

-- 2.3 apelidos(AS) e colunas calculadas
select nome as produto, preco as  preco_atual,
	preco * estoque as valor_em_estoque
from produtos;

-- 3.1 igualdade
select * from clientes
where cidade = 'são paulo';

-- 3.2 comparaçãoptimize
select nome, preco from produtos
where preco > 2000; -- notebook

-- 3.3 AND: as duas condições precisam ser verdadeiras
select nome, preco, estoque from produtos
where preco > 1000 and estoque < 10; -- Cadeira Gamer

-- 3.4 OR; Basta uma ser verdadeira
select nome, categoria, preco from produtos
where categoria = 'Móveis' or preco > 3000; -- os dois produtos

-- 3.5 IN - lista de valores
select nome, estado from clientes
where estado in ('SP', 'RJ'); -- Carlos

-- 3.6 BETWEEN - intervalo (inclui extremidades)
select id, data_pedido, status from pedidos
where data_pedido between '2025-07-01' and '2025-07-31';

select * from clientes;
-- 3.7 LIKE - busca por padrão
-- % = qualquer quantidade de caracteres
select nome from clientes where nome like 'C%'; -- começa com c
select nome from produtos where nome like '%gamer%'; -- carlos

-- 3.8 IS NULL/ IS NOT NULL
-- ATENÇÃO: "email = NULL" NÃO funciona. Use sempre IS NULL
select * from clientes where email is null; -- Ana
select * from clientes where email is not null -- Carlos

-- 3.9 NOT - nega a condição
select id, status from pedido;
where not status = 'pendente'; -- pedido 1

#4 DISTINCT - removendo repetições;
select * from pedidos; -- o cliente 1 aparece 2x
select distinct cliente_id from pedidos; -- o cliente aparece 1x

#5 ORDER BY - ordenando resultados
select nome, preco from produtos
order by preco desc; -- do mais caro ao mais barato

select nome, preco from produtos
order by preco asc; -- do mais barato a mais caro

-- ordenação por mais de uma coluna
-- primeiro por estado (A->Z) e, dentro dele, por nome (A->Z)
select estado

#6 limit

-- 6.1 o produto mais caro
select nome, preco from produtos
order by preco desc
limit 1; -- Notebook

-- 6.2 OFFSET: pula 1 linha
-- usado para paginação
select nome, preco from produtos
order by preco desc
limit 1 offset 1; -- cadeira gamer

#7. FUNÇÕES DE AGREGAÇÃO - COUNT, SUM, AVG, MAX, MIN


-- 7.1 COUNT(*) conta linhas; COUNT(coluna) ignora NULL
select count(*) as total_clientes, -- 2
    count(email) as clientes_com_email -- 1 (o e-mail da Ana é NULL)
    from clientes;
    
-- 7.2 SUM - valor total vendido (quantidade x preço de cada item)
select sum(quantidade * preco_unitario) as faturamento_total
from itens_pedido; -- 3500 + 2400 = 5900.00


-- 7.3 AVG - preço médio (ROUND arrendonda pra 2 casas)
select round(avg(preco), 2) as preco_medio
from produtos; -- 2350.00

-- 7.4 MAX e MIN
select max(preco) as mais_caro, -- 3500.00
        min(preco) as mais_barato -- 1200.00
from produtos; 

-- 7.5 Agregação com filtro
select sum(estoque) as unidades_informatica
from produtos
where categoria = 'Informática'; -- 10

-- 7.6 Descobrindo QUAL produto tem o maior preço (subconsulta)
select nome, preco from produtos
where preco = (select max(preco) from produtos); -- Notebook
