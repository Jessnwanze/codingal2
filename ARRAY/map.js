// Step 1: Create an array of numbers
let numbers = [12, 5, 8, 130, 44, 61, 72];

// Step 2: Use map() to apply a transformation (let's square each number)
let mappedNumbers = numbers.map(num => num * num);

// Step 3: Sort the mapped array in ascending order
let ascendingOrder = [...mappedNumbers].sort((a, b) => a - b);

// Step 4: Sort the mapped array in descending order
let descendingOrder = [...mappedNumbers].sort((a, b) => b - a);

// Step 5: Display the results
console.log("Original numbers:", numbers);
console.log("Mapped numbers (squared):", mappedNumbers);
console.log("Mapped numbers in ascending order:", ascendingOrder);
console.log("Mapped numbers in descending order:", descendingOrder);
