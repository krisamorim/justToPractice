/*
//lenth -> show the number of characters
let anString = "This is a text";
console.log(anString.length)
//or directly on console 
console.log("this is another text".length)

//indexOf -> search some info inside the strings
console.log(anString.indexOf("text"))

//slice ->
console.log(anString.slice(0,4))

//get word night inside a string
let phrase = "Good night";

function fastReplacement(text, wordSearched, wordReplaced){
  return text.replace(wordSearched, wordReplaced)
}

console.log(fastReplacement(phrase, "night", "afternoon"))

//get name kris from an object - just to practice
//creating an object
let me = {
  name: "Kris",
  age: 35,
  city: "london"
}

//converting to string
me = JSON.stringify(me);

//get the kris position
let name = me.indexOf("Kris");

//cut the string from position 9 to 13
console.log(me.slice(name,13))


//practice Nov 15
//creating an object
let me = {
  name: "Kris",
  age: 35,
  city: "London"
};
//showing onbject
console.log(me);

console.log("\nget the name from an object: "+me.name+"\n");

//converting to string
me = JSON.stringify(me);
 
console.log("afert converted to string: "+me+"\n");

//searching position name
let positionName = me.indexOf("name");

//get the name's end position
let positiAfetNam = 7+positionName;

 //show name
 let name = me.slice(positiAfetNam,positiAfetNam+4)
console.log("name is: "+name+"\n");

//replace name kris
let ana = me.replace(name, "Ana");
console.log(ana)
console.log("")

//convertin ana go object
ana = JSON.parse(ana);

//show object
console.log(ana)
console.log("")

//----------------------converting string in to array
//creating array
var thisIsString = "God bless you you you";

//show before convetion
console.log(thisIsString);

//using split to  variable to receive ceonvertion 
let convertedToArray = thisIsString.split(' '); 

//show after convertion
console.log(convertedToArray)

//replace the first YOU element found
console.log(thisIsString.replace(/you/g, ""));
console.log(thisIsString.replace(/ /g, '-'));

*/

//another way (a bad way) to chande the name in a string
//creatin an object
let me = {
  name: "Kris",
  age: 35,
  city: "London"
};

//converting to string and after split then creating an array
me = JSON.stringify(me).split(",");
console.log(me+"\n")
//position double dot
let positDoubleDot = me[0].indexOf(":");
console.log(positDoubleDot)

//get characters qty
let qtyCharacters = me[0].length;
console.log(qtyCharacters)

//get the name
let name = me[0].slice(positDoubleDot+2,qtyCharacters-1)

console.log(me)
//convert to string and replace name
me = JSON.stringify(me).replace(name, "Pedro")

//back to array
me = JSON.parse(me)
console.log(me)