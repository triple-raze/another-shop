const username = document.getElementById('username')
const email = document.getElementById('email')
const password = document.getElementById('password')
const password_repeat = document.getElementById('password_repeat')



fetch("auth/register", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value
    })
})
.then(res => res.json())
.then(data => console.log(`Ответ: ${data}`))
.catch(error => console.log(`Ошибка: ${error}`))
