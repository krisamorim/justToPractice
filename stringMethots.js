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
  return phrase.replace(wordSearched, wordReplaced)
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