'use strict'

const switcher = document.querySelector('.btn');
// função click do botão para trocar
switcher.addEventListener('click', function() {
    document.body.classList.toggle('dark-theme')//Trocar para dark theme (padrão é o light)

    var classname = document.body.className;
    if(classname == "light-theme") {
        this.textContent = "Escuro";
    }
    else{
        this.textContent = "Claro"; // if e else para trocar texto do botão
    }
});
