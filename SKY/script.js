// You can add JavaScript to make the sun's movement interactive
// For example, change the sun's position based on mouse movements

document.querySelector('.sky').addEventListener('mousemove', function (event) {
    const sun = document.querySelector('.sun');
    const x = event.clientX / window.innerWidth;
    const y = event.clientY / window.innerHeight;

    const sunPosX = (x * 100) - 10; // Adjust sun's x position
    const sunPosY = (y * 100) - 10; // Adjust sun's y position

    sun.style.left = `${sunPosX}%`;
    sun.style.top = `${sunPosY}%`;
});
