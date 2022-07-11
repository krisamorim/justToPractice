fun main() {
    //variavel mutavel
    var variavelX = "Kris"
    var idade = "38"

    //variavel imutatel
    val pi = 3.14
    println("Varaiáveil e seu valores:\nVariavel: "+variavelX+"\n"+"Constante: "+pi+"\nIdade: "+idade+"\n---------------------------------------------------------------------------------")

    //mostrar os tipos utilizando ::clas
    println("Variaveis e seus tipos:\nvariavelX: "+variavelX::class)
    println("pi: "+pi::class)
    println("idade: "+idade::class)
}