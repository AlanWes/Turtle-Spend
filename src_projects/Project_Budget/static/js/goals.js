/// FOR CSS

///MOBILE MENU BTN

const menubtn = document.querySelector(".menu-btn")
const navLinks = document.querySelector(".nav-links")

menubtn.addEventListener('click',()=>{
navLinks.classList.toggle('mobile-menu')
})