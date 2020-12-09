/*
Faça um SQL que busque todas as locações deste mês com as seguintes colunas:
filme.nome, genero.nome, locacao.dtlocacao, usuario.nome, usuario.email

Pegando as principais tabelas da base, utilizando o join entre as mesmas.
Utilizando as chaves estrangeiras, temos as seguintes consultas abaixo.

*/

select filme.nome, genero.nome, locacao.dtlocacao, usuario.nome, usuario.email from filme
inner join genero
on genero.id = filme.generoid
inner join filmelocacao
on filmelocacao.filmeid = filme.id
inner join locacao
on locacao.filmelocacaoid = filmelocacao.id
inner join usuario
on usuario.id = locacao.usuarioid
where month(locacao.dtlocacao) = '12';

/* ou */

select filme.nome, genero.nome, locacao.dtlocacao, usuario.nome, usuario.email
from filme
inner join genero
on genero.id = filme.generoid
inner join filmelocacao
on filmelocacao.filmeid = filme.id
inner join locacao
on locacao.filmelocacaoid = filmelocacao.id
inner join usuario
on usuario.id = locacao.usuarioid
where locacao.dtlocacao between '2020-12-01' and '2020-12-31';

/*

Faça um SQL que apresente todos os usuário inativos que já tiveram alguma locação com as seguintes colunas:
usuario.nome, usuario.cpf

*/

select distinct usuario.nome, usuario.cpf
from filme
inner join filmelocacao
on filmelocacao.filmeid = filme.id
inner join locacao
on locacao.filmelocacaoid = filmelocacao.id
inner join usuario
on usuario.id = locacao.usuarioid
where usuario.ativo = 0;

/*

Faça um SQL que apresente a filmes alugados por usuario que contem a letra "A" em seu email com as seguintes colunas:
filme.id, filme.nome

Usando o comando join, para pegar as tabelas envolvidas para a consulta.
O comando LIKE, é para pegar a letra ou palavras informadas dentro do que foi pedido.
Colocando o "%", a consulta busca na coluna a informação solicitada, exemplo
like '%A%': procura no campo onde a plavra possua a letra "A";
like 'A%': procura no campo onde a palavra comece pela letra "A";
like '%A': procura no campo onde a palavra termine pela letra "A"

*/

select filme.id, filme.nome, usuario.email, usuario.nome from filme
inner join locacao
on locacao.filmelocacaoid = filme.id
inner join usuario
on usuario.id = locacao.usuarioid
where usuario.email like '%A%';

/*

Faça um SQL que apresente os filmes mais alugados:
filme.nome, quantidade de alugueis

*/

select filme.nome, count(1) 'quantidade de alugueis'
from filme
inner join filmelocacao
on filmelocacao.filmeid = filme.id
inner join locacao
on locacao.filmelocacaoid = filmelocacao.id
inner join usuario
on usuario.id = locacao.usuarioid
group by filme.nome
order by count(1) desc