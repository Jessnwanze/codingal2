// Get elements from the DOM
const balanceElement = document.getElementById('balance');
const amountInput = document.getElementById('amount');
const depositButton = document.getElementById('deposit-btn');
const withdrawButton = document.getElementById('withdraw-btn');
const messageElement = document.getElementById('message');

// Initial balance
let balance = 1000.00;

// Update balance display
function updateBalance() {
    balanceElement.textContent = balance.toFixed(2);
    messageElement.textContent = ''; // Clear any messages
}

// Show message
function showMessage(message, type = 'error') {
    messageElement.textContent = message;
    messageElement.style.color = type === 'error' ? 'red' : 'green';
}

// Deposit money
function deposit() {
    const amount = parseFloat(amountInput.value);
    if (isNaN(amount) || amount <= 0) {
        showMessage('Please enter a valid amount to deposit');
        return;
    }
    balance += amount;
    updateBalance();
    showMessage(`$${amount.toFixed(2)} deposited successfully!`, 'success');
    amountInput.value = ''; // Clear input field
}

// Withdraw money
function withdraw() {
    const amount = parseFloat(amountInput.value);
    if (isNaN(amount) || amount <= 0) {
        showMessage('Please enter a valid amount to withdraw');
        return;
    }
    if (amount > balance) {
        showMessage('Insufficient balance for withdrawal');
        return;
    }
    balance -= amount;
    updateBalance();
    showMessage(`$${amount.toFixed(2)} withdrawn successfully!`, 'success');
    amountInput.value = ''; // Clear input field
}

// Event listeners for buttons
depositButton.addEventListener('click', deposit);
withdrawButton.addEventListener('click', withdraw);

// Initialize balance on load
updateBalance();

    