const numDivs= 48;
for (let i = 1; i <= numDivs; i++) {
    let div = document.createElement('div');
    div.className = 's';
    const delay = (i * 3) / 48;
    const hue = 360 - (i*360) / 48;
    const borderColor = 'hsla(${hue}, 100%, 50%, 1)';
    div.style.borderColor = borderColor;
    document.body.appendChild(div);
}