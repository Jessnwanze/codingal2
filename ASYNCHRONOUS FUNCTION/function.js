// Simulate an asynchronous operation (like fetching data)
async function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Data from the server");
        }, 2000);  // Simulate 2 seconds of delay
    });
}

// Function that depends on the result of fetchData
async function processData() {
    try {
        // Wait for the result of fetchData
        const data = await fetchData();

        // Now you can use the result of fetchData to process the data
        console.log("Processing the following data:", data);

        // You can return or further process the data if necessary
        return `Processed: ${data}`;
    } catch (error) {
        console.error("Error processing data:", error);
    }
}

// Call the processData function
processData().then((result) => {
    console.log(result);  // This will log the processed result
});
