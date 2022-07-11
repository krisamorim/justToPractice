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
}

class Filme {
    var titulo: String = ""
    var descricao: String = ""
    var elenco: String = ""
}