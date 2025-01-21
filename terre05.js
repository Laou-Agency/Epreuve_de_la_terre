const dividend = parseInt(process.argv[2]);
const divisor = parseInt(process.argv[3]);

const quotient = dividend / divisor;
const remainder = dividend % divisor;

if (divisor === 0) {
   return console.log("error");
} else if(dividend < divisor){
    return console.log("error");
}
console.log(`Quotient: ${parseInt(quotient)}\nRemainder: ${parseInt(remainder)}`);