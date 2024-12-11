function validates(e) {
e.preventDefault();

const email = document.getElementById('email').value;
const pass = document.getElementById('password').value;
const age = document.getElementById('age').value;
const msgBox = document.getElementById('message');

let message = '';

if (email === '') {
    message = 'enter an email.';
    msgBox.style.color = 'black';
} else if (pass === '') {
    message = 'enter a password';
    msgBox.style.color = 'red';
} else if (age === '') {
    message = 'enter your age';
    msgBox.style.color = 'orange';
} else {
    message = 'Login successful!';
    msgBox.style.color = 'green';
}

msgBox.innerText = message;
}