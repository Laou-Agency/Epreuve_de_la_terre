let number = process.argv.slice(2);
// Si la taille de mon tableau est vide afficher "tu ne me la mettras pas à l'envers."
if (number.length === 0) {
    console.log("Tu ne me la mettras pas à l'envers.");
} else {
    let n = Number.parseInt(number[0]); // Convertir l'entrée str en int
    if (Number.isNaN(n)){ // Vérifier que l'entrée est une str
        console.log("Tu ne me la mettras pas à l'envers.");
    } else if (n % 2 === 0) { // Vérifier que le nombre est pair ou impair
        console.log(`${n} pair`);
    } else {
        console.log(`${n} impair`);
    }   
}
