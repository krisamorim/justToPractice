fun main() {
    //criadno objeto A e instanciando o mesmo
    val userA = User()

    userA.varName = "kris"

    userA.printUpperCase()

    userA.updateName("Ana")

    userA.printUpperCase()

    val userAnameLength = userA.getNameLength()

    println(userAnameLength)





}