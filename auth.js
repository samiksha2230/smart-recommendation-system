async function signupUser() {

    const username = document.getElementById(
        "signup-username"
    ).value;

    const email = document.getElementById(
        "signup-email"
    ).value;

    const password = document.getElementById(
        "signup-password"
    ).value;

    const response = await fetch(
        "http://127.0.0.1:8000/signup",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                email: email,
                password: password
            })
        }
    );

    const data = await response.json();

    alert(data.message);

    if (data.message === "User created successfully") {

        window.location.href = "login.html";
    }
}

async function loginUser() {

    const username = document.getElementById(
        "username"
    ).value;

    const password = document.getElementById(
        "password"
    ).value;

    const response = await fetch(
        "http://127.0.0.1:8000/login",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                password: password
            })
        }
    );

    const data = await response.json();

    if (data.message === "Login successful") {

        localStorage.setItem(
            "username",
            data.username
        );

        window.location.href = "home.html";
    }
    else {

        alert(data.message);
    }
}