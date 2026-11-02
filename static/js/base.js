// base.js - comportamiento común a todas las páginas
(function () {
  'use strict';

  // Los mensajes (éxito, error, etc.) se cierran solos a los 5 segundos o al hacer clic.
  var mensajes = document.querySelectorAll('.mc-mensajes li');

  function ocultar(li) {
    li.classList.add('oculto');
    setTimeout(function () { li.remove(); }, 400);
  }

  mensajes.forEach(function (li) {
    li.addEventListener('click', function () { ocultar(li); });
    setTimeout(function () { ocultar(li); }, 5000);
  });
})();
