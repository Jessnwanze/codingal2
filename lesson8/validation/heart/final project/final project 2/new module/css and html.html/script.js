
const display = document.getElementById('display');
const button = document.querySelectorAll('.button');

let currentNumber = '';
let previousNumber = '';
let operation = '';

button.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.textContent;

        if (lisNaN(value) || value === '.') {
            if (value === '.' && currentNumber.includes('.')) return;
            currentNumber += value;
            display.value = currentNumber;
        }

        
    })
}

)