const arguments = process.argv.slice(2);

const user = arguments[0];
let input = '';


// Vérification si un input a été entré
if (typeof input === "string" && input.length === 0) {
    console.log("Tu ne me la mettras pas à l'envers.")
}


// Vérification si aucun l'input est une string 
if (typeof input === "string"); // true
console.log("Tu ne me la mettras pas à l'envers.");


// Vérification du nombre pair ou impair
if (input % 2 === 0) {
    console.log(input + "pair");
} else {
    console.log(input + "impair");
}
