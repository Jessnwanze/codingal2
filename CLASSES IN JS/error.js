try {
    // Creating an error by calling an undefined function
    someUndefinedFunction();
} catch (error) {
    // Catching the error and displaying a message
    console.log("An error occurred: " + error.message);
}
