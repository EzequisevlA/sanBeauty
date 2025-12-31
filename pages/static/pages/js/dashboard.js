document.addEventListener("DOMContentLoaded", () => {

    // Função auxiliar para carregar conteúdo (Evita repetição)
    const loadContent = (url, containerId) => {
        const container = document.getElementById(containerId);
        if (!container) return;

        fetch(url)
            .then(response => {
                if (!response.ok) throw new Error("Erro ao carregar página");
                return response.text();
            })
            .then(html => {
                container.innerHTML = html;
                container.style.display = 'block';
            })
            .catch(err => console.error("Erro na requisição:", err));
    };

    // LOGOUT
    const btnLogout = document.getElementById("btn_logout");
    if (btnLogout) {
        btnLogout.onclick = () => {
            fetch(btnLogout.dataset.url, { method: "GET" })
                .then(() => window.location.href = '/');
        };
    }

    // CONFIGURAÇÃO
    const btnConfig = document.getElementById("btnConfig");
    if (btnConfig) {
        btnConfig.addEventListener("click", () => {
            loadContent("/configuration/", "card_customers");
        });
    }

    // LISTAR CLIENTES
    const btnClientes = document.getElementById("btnClientes");
    if (btnClientes) {
        btnClientes.addEventListener("click", () => {
            loadContent("/customers/list/", "card_customers");
        });
    }
});

// CARD TEMPLATE
function changeCard() {
    const container = document.getElementById('card_customers');
    const template = document.getElementById('template_card');

    if (container && template) {
        const clone = template.content.cloneNode(true);
        container.innerHTML = ''; // Limpa o conteúdo atual
        container.appendChild(clone);
    }
}
