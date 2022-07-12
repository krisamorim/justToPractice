fun main() {
    //iniciando a varaialvel
    val userA = Usuario()
    val userB = Usuario()

    //utilizando a propriedade nome da class Usuário
    userA.nome = "Kris"
    userB.nome = "Ana"

    //mostrando o valor
    println(userA.nome)

    //aqui podemos ver a utilizando da função imprimirCaixaAlta do objeto Usuário
    userA.imprimirCaixaAlta()
    userB.imprimirCaixaAlta()

    //utilizando get
    println(userA.getNomeEmCaixaBaixa())

    //utilizando propriedade de atualizar nome
    userA.atualizarNome("Pedro")

    //mostrando como criar um objeto com mais de uma propriedade
    val botaoSucesso = Botao()
    botaoSucesso.texto = "Sucesso"
    botaoSucesso.cor = "Green"

    val botaoCancelar = Botao()
    botaoCancelar.texto = "Cancelar"
    botaoCancelar.cor = "Red"

    //objeto com mais de uma propriedade
    val filmeVingadores1 = Filme()
    filmeVingadores1.titulo = "Os Vingadores"
    filmeVingadores1.descricao = "O Filme conta a origem dos vingadores"
    filmeVingadores1.elenco = "Scarlett Johansson, Chris Evans, Mark Ruffalo, Robert Downey, CHris Hemsworth, Samuel L Jackson, Jeremy Renner"
}

class Usuario {
    //propriedade
    var nome: String = ""

    //resopnsabilidades (uma função para transofrma em caixa alta)
    fun imprimirCaixaAlta(){
        println("Variavel em caixa alta: " + nome.uppercase())
    }

    fun getNomeEmCaixaBaixa(): String{
        return nome.lowercase()
    }

    //atualiza o valor da variavel nome e mostra mensagem no console
    fun atualizarNome (novoNome: String){
        var nomeAntigo = nome
        nome = novoNome
        println("Nome atualizado de $nomeAntigo para $nome")
    }
}

class Botao {
    var texto: String = ""
    var cor: String = ""
}

//criando um objeto com mais de uma propriedade
class Filme {
    var titulo: String = ""
    var descricao: String = ""
    var elenco: String = ""
}