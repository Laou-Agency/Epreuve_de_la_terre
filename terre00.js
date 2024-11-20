// les étapes
// créer une boucle 
// parcourt tout l'alphabet lettre par lettre
const numberA = 97
const numberZ = 122
let alphabet = ""
// 
for (let i = numberA; i <= numberZ; i++) {
   
    alphabet += String.fromCharCode(i);
   
}
console.log(alphabet)