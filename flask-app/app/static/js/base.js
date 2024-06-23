// script.js

// Função para ajustar o tamanho do conteúdo com base no tamanho da viewport
function adjustViewport() {
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;

    const content = document.getElementById('main');

    // Aqui, você pode ajustar o estilo conforme necessário
    content.style.width = `${viewportWidth}px`;
    content.style.height = `${viewportHeight}px`;
}

// Chamar a função quando a página é carregada
window.addEventListener('load', adjustViewport);

// Chamar a função quando a janela é redimensionada
window.addEventListener('resize', adjustViewport);
