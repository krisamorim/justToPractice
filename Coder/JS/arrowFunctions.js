//phrase
let phase = "Have a good night";

//####### replace word ####### 
// ->> nornal function sintax 
function substituir (text, wordSearched, wordToReplace){
  return text.replace(wordSearched, wordToReplace)
}

console.log(substituir(phase, "night", "morning"))

//with arrow function 
const troca = (text, wordSearched, wordToReplace) => text.replace(wordSearched, wordToReplace)

console.log(troca(phase, "night", "afternoon"))


// ####### search if there is a specific word #######
// ->> normal function sintax
function searchWord(text, word){
  if(text.indexOf(word) !== -1) {
    return  true
  }else{
    return false
  }
}

// ->> arrow function
let searchingWord = (text, word) => text.indexOf(word) !== -1 ? true : false;
console.log(searchingWord(phase, "night"))


// ####### Show current time #######
// ->> normal sintax
function time() {
  let data = new Date();
  return `${data.getHours()}:${data.getMinutes()}`;
}
console.log(time())


// ->> arrow function
let currentTime = () => {
  let data = new Date();
  return `${data.getHours()}:${data.getMinutes()}`;
}
*/

