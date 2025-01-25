class BankAccount {
    constructor() {
        this.balance = 0;
        this.income = 0;
        this.expenses = 0;
        this.transactions = [];
    }

    // Method to add income
    addIncome(amount) {
        if (amount > 0) {
            this.balance += amount;
            this.income += amount;
            this.transactions.push(`Income: $${amount}`);
            console.log(`Added Income: $${amount}`);
        } else {
            console.log("Income amount must be greater than zero.");
        }
    }

    // Method to add expense
    addExpense(amount) {
        if (amount > 0) {
            this.balance -= amount;
            this.expenses += amount;
            this.transactions.push(`Expense: $${amount}`);
            console.log(`Added Expense: $${amount}`);
        } else {
            console.log("Expense amount must be greater than zero.");
        }
    }

    // Method to get balance
    getBalance() {
        console.log(`Current Balance: $${this.balance}`);
    }

    // Method to get the total income
    getIncome() {
        console.log(`Total Income: $${this.income}`);
    }

    // Method to get total expenses
    getExpenses() {
        console.log(`Total Expenses: $${this.expenses}`);
    }

    // Method to view all transactions
    viewTransactions() {
        console.log("Transactions:");
        this.transactions.forEach(transaction => {
            console.log(transaction);
        });
    }
}

// Example usage of the BankAccount class
let myAccount = new BankAccount();

myAccount.addIncome(1000);
myAccount.addExpense(200);
myAccount.addIncome(500);
myAccount.addExpense(150);

myAccount.getBalance();      // View current balance
myAccount.getIncome();       // View total income
myAccount.getExpenses();     // View total expenses
myAccount.viewTransactions(); // View all transactions
