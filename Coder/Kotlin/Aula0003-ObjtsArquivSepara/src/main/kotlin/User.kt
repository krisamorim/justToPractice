class User {
    //property name
    var varName: String = ""
    var varCpf: String = ""

    //responsibility
    fun printUpperCase(){
        println("Hi " + varName.uppercase())
    }

    //responsibility
    fun updateName(newName: String){
        var lastName = varName
        varName = newName
        println("Name updated from $lastName to $newName");
    }

    //count character
    fun getNameLength() : Int{
        return varName.length
    }
}