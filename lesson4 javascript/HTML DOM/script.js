function validates(e) {
e.preventDefault();

const email = document.getElementById('email').Value;
const pass = document.getElementById('password').Value;
const age = document.getElementById('age').value;
const msgBox = document.getElementById('message').value;

let message = '';

if (email === '') {
    message = 'enter an email.';
    msgBox.style.color = 'yellow';
} else if (pass === '') {
    message = 'enter a password';
    msgBox.style.color = 'red';
} else if (age === '') {
    message = 'enter your age';
    msgBox.style.color = 'orange';
} else {
    message = 'Login successful!';
    msg.style.color = 'green';
}

msgBox.innerText = message;
}