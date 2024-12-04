const arguments = process.argv.slice(2)


// print processs.argv
const a = String.fromCharCode(97);
const m = String.fromCharCode(109);
const n = String.fromCharCode(110);
const z = String.fromCharCode(122);
let alphabet = '';
let retourALaLigne = "\n";

var i;
for (let i = 97; i <= 122; i++) {
    if (i >= 110)
    alphabet += String.fromCharCode(i);
}
console.log(alphabet);
console.log(retourALaLigne);
