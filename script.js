async function loginUser(){

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch(
        `http://127.0.0.1:8000/login?username=${username}&password=${password}`,
        {
            method: "POST"
        }
    );

    const data = await response.json();

    document.getElementById("message").innerText = data.message;
}