// app.js
const apiUrl = 'http://localhost:5000/api';

// Fetch user details by ID
async function getUserDetails() {
    const userId = document.getElementById('userId').value;
    if (!userId) return alert('Please enter a User ID');

    const response = await fetch(`${apiUrl}/user/${userId}`);
    const data = await response.json();

    if (data.message) {
        alert(data.message);
        return;
    }

    document.getElementById('userName').innerText = `Name: ${data.name}`;
    document.getElementById('userBalance').innerText = `Balance: $${data.balance}`;
    document.getElementById('accountInfo').style.display = 'block';
}

// Deposit money into the account
async function deposit() {
    const userId = document.getElementById('userId').value;
    const amount = document.getElementById('depositAmount').value;

    const response = await fetch(`${apiUrl}/deposit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: userId, amount: parseFloat(amount) })
    });

    const data = await response.json();
    if (data.message) {
        alert(data.message);
        return;
    }

    document.getElementById('userBalance').innerText = `Balance: $${data.balance}`;
    alert(data.message);
}

// Withdraw money from the account
async function withdraw() {
    const userId = document.getElementById('userId').value;
    const amount = document.getElementById('withdrawAmount').value;

    const response = await fetch(`${apiUrl}/withdraw`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: userId, amount: parseFloat(amount) })
    });

    const data = await response.json();
    if (data.message) {
        alert(data.message);
        return;
    }

    document.getElementById('userBalance').innerText = `Balance: $${data.balance}`;
    alert(data.message);
}
