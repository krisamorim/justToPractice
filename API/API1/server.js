const { json } = require('express');
const express = require('express'); //importando express
const app = express();//instaciando express na variável app
const data = require("./data.json");//importando dados

app.use(express.json()); //informando ao express que irei usar o metodo json

//criando o server
app.listen(3000, function(){
  console.log("Server is running")
})

/*
Verbos HTTP
  GET -> recebe dados de um resource
  POST -> envia dados que serão processados pelo resource
  PUT -> atualiza dados de um resource
  DELETE -> deleta resource

Conceitos
  http://localhost:3000/clients

  URI -> é localhost:3000/clients
  endpoint -> o que vem após a uri (no caso aqui é clients)
  resource -> clients
*/

//usando os verbos
//add o endpoint ("/clients") em cada um dos verbos 
app.get("/clients", function(req, res){
  res.json(data);
});//pegar todos os clientes

app.get("/clients/:id", function(req, res){
  const { id } = req.params; //pegando o id do cliente do uri
  const client = data.find(cli => cli.id = id);//buscando o cliente com o id pego da URI e associando à variável client o id com o mesmo id pego dos parâmetros da URI
  
  //se não existir o clinet
  if (!client) return res.status(204).json();
  res.json(client);//respondendo o client encontrado
});//pegar um cliente

app.post("/clients", function(req, res){
  const { name, email } = req.body;//pegar name e email do body
  //salvar
  res.json({ name, email});
});//salvar um cliente

app.put("/clients/:id", function(req, res){

  const { id } = req.params;
  const client = data.find(cli => cli.id = id);

  if (!client) return res.status(204).json();

  const { name } = req.body;
  client.name = name;

  res.json(client);

});//atualizar um cliente

app.delete("/clients/:id", function(req, res){
   const { id } = req.params;
   const clientsFiltered = data.filter(client => client.id != id);

   res.json(clientsFiltered);
});//deletar um cliente

/*
- 1xx: Informação
- 2xx: Sucesso
  - 200: ok
  - 201: Created
  - 204: Não tem conteudo PUT POST DELETE
- 3xx: Redirection
- 4xx: Client error
  - 400: Bad Request
  - 404: Nof Found
- 5xx: Serer error
  - 500: Internal Server error
*/