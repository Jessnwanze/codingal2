// Declare an empty set to store random numbers
let randomNumbers = new Set();

// Generate random numbers between 1 and 100 and add to the set until it contains 5 unique numbers
while (randomNumbers.size < 5) {
    let randomNumber = Math.floor(Math.random() * 100) + 1; // Generates a random number between 1 and 100
    randomNumbers.add(randomNumber); // Adds the random number to the set
}

// Print the set of random numbers
console.log("Set of random numbers:", Array.from(randomNumbers));
