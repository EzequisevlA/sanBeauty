var btn_login = document.getElementById("btn");
const url = btn_login.dataset.url;  // Pega a URL do atributo data-url

btn_login.onclick = function(){
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(url, {  // usa a URL correta
        method:"POST",
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({username, password})
    })
    .then(response => response.json())
    .then(data => {
        if(data.success){
            window.location.href = "/add_customer/";
        } else {
            document.getElementById("error").innerText = "Usuário ou senha inválidos";
        }
    });
}

