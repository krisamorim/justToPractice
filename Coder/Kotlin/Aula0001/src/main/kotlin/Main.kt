fun main() {
    //variavel mutavel
    var variavelX = "Kris"
    var idade = "38"

    //variavel imutatel (constante)
    val pi = 3.14
    println("Varaiáveil e seu valores:\nVariavel: "+variavelX+"\n"+"Constante: "+pi+"\nIdade: "+idade+"\n---------------------------------------------------------------------------------")

    //declarando variavel especificando o tipo
    var carroModelo: String = "Jeep"
    var carroKm: Double = 31.900
    var carroAno: Int = 2022

    //mostrar os tipos utilizando ::clas
    println("Variaveis e seus tipos:\nvariavelX: "+variavelX::class)
    println("pi: "+pi::class)
    println("idade: "+idade::class+"\n---------------------------------------------------------------------------------")

    //mostrar variaveis tipadas
    println(carroModelo+"\n"+carroKm+"\n"+carroAno)

    //outros tipos
    val var1: Byte = 8 //ocupa 8bits
    val var2: Short = 16 //ocupa 16 bits
    var var3: Float = 32.1f //ocupa 32 bit
    val var4: Long = 64 //ocupa 64 bits
    var var5: Double = 64.1 //ocupa 64 bits
    var var6: Boolean = true //ocupa 1byte (mesmo não utilizando os 8 bits) 0- false e 1 - true

    //conversão
    //int p/ double
    var numInt = 10
    println("aqui a variavel é "+numInt::class)
    var intParaDouble = numInt.toDouble()
    println("aqui a variavel é "+intParaDouble::class)
}