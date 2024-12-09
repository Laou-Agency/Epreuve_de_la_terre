const arguments = process.argv.slice(2);

const firstLetter = arguments[0];
const asciiConverter = firstLetter.charCodeAt(0);

const numberA = String.fromCharCode(97);
const numberZ = String.fromCharCode(122);

let alphabet = '';
let retourALaLigne = "\n";

for (let i = asciiConverter; i <= numberZ; i++) {
    alphabet += String.fromCharCode(i);
}
console.log(alphabet);
