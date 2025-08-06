// регистация аккаунта
fetch(
    auth/register, {
        method: POST,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            {
                "key": "value"
            }
        ),
    }
)
.then(response => response.json())
.then(
    data => {
        //здесь код
    }
)
.catch(
    error => console.log(
        error
    )
)



// вход в аккаунт
fetch(
    auth/login, {
        method: POST,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            {
                "key": "value"
            }
        ),
    }
)
.then(response => response.json())
.then(
    data => {
        //здесь код
    }
)
.catch(
    error => console.log(
        error
    )
)



// выход из аккаунта
fetch(
    auth/logout, {
        method: POST,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            {
                "key": "value"
            }
        ),
    }
)
.then(response => response.json())
.then(
    data => {
        //здесь код
    }
)
.catch(
    error => console.log(
        error
    )
)



// перевыпуск аккаунта
fetch(
    auth/refresh, {
        method: POST,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(
            {
                "key": "value"
            }
        ),
    }
)
.then(response => response.json())
.then(
    data => {
        //здесь код
    }
)
.catch(
    error => console.log(
        error
    )
)