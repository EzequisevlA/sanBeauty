document.addEventListener("DOMContentLoaded", () => {

    // LOGOUT
    const btn_logout = document.getElementById("btn_logout");
    if (btn_logout) {
        btn_logout.onclick = function () {
            const url = btn_logout.dataset.url;
            fetch(url, { method: "GET" })
                .then(() => window.location.href = '/');
        };
    }

    // LISTAR CLIENTES
    const btnClientes = document.getElementById("btnClientes");
    if (!btnClientes) return;

    btnClientes.addEventListener("click", () => {
        const container = document.getElementById("card_customers");

        fetch("/customers/list/")  // URL REAL
            .then(response => response.text())
            .then(html => {
                container.innerHTML = html;
                container.style.display = "block";
            })
            .catch(err => console.error(err));
    });
});

// CARD
function changeCard() {
    const card_container = document.getElementById('card_customers');
    const temporary = document.getElementById('template_card');

    if (!temporary) return;

    const clone = temporary.content.cloneNode(true);
    card_container.innerHTML = '';
    card_container.appendChild(clone);
    //card_container.classList.add("card_customers--agend");//
}
