


// Check if number is even or odd
let number = process.argv.slice(2);
// si la taille de mon tableau est vide afficher "tu ne me la mettras pas à l'envers."
if (number.length === 0) {
    console.log("Tu ne me la mettras pas à l'envers.");
} else {
    let n = Number.parseInt(number[0]);
    if (Number.isNaN(n)){
        console.log("Tu ne me la mettras pas à l'envers.");
    } else if (n % 2 === 0) {
        console.log(`${n} pair`);
    } else {
        console.log(`${n} impair`);
    }   
}


    //console.log("Tu ne me la mettras pas à l'envers.");