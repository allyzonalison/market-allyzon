'use strict';

const btnLogin = document.querySelector('.profile-login-icon');
const btnAddToCart = document.querySelector('.add-to-cart-icon');

btnLogin.style.color = '#8D703D';
btnAddToCart.style.color = '#8D703D';

btnLogin.addEventListener('click', function() {
    window.location.href = 'login.html';
});

btnAddToCart.addEventListener('click', function() {
    window.location.href = 'add-to-cart.html';
});