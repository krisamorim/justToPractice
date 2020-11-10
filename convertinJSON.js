//An objetc | Un objet
let me = {
  name: "Kris",
  age: 35,
  city: "London",
}

//showing variabel me | Montrant la variable
console.log("\nThe variable like an object\nLa variable comme un objet")
console.log(me)

//Converting to JSON | Conversion en JSON
me = JSON.stringify(me);

//showing variable me converted | montrant la variable me convertie
console.log(`\nAfter conversion to string \nAprès conversion en chaîne \n ${me}`);

//Back to the object | Retour à l'objet
me = JSON.parse(me)

//showing the variable me back to object | montrant la variable me retour à l'objet
console.log("\n Showing the variable back to object\nmontrant la variable retour à l'objet")
console.log(me)