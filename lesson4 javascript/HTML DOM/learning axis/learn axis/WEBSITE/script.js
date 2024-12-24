// JavaScript for scroll-to-top button
window.onscroll = function () {
    showScrollButton()
};

function showScrollButton() {
    const scrollButton = document.getElementById("scrollBtn");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        scrollButton.style.display = "block";
    } else {
        scrollButton.style.display = "none";
    }
}

function scrollToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// Add the scroll button to HTML
document.body.innerHTML += `<button id="scrollBtn" onclick="scrollToTop()" style="display:none; position:fixed; bottom:20px; right:20px; background-color: #ff5733; color: white; padding: 15px 20px; border: none; border-radius: 50%; font-size: 16px;">↑</button>`;
