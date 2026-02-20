document.addEventListener("DOMContentLoaded", function () {

    const menuBtn = document.getElementById("mobileMenuBtn");
    const navLinks = document.querySelector(".nav-links");

    if (menuBtn) {
        menuBtn.addEventListener("click", function () {
            navLinks.classList.toggle("active");
        });
    }

});
