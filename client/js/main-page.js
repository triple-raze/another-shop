fetch("/users", {
method: "POST",
headers: {"Content-Type": "application/json"},
body: JSON.stringify(user: document.getElementById("tovary").value
})
.then(response => response.json())
.then(data  => console.log(data))
.catch(error => console.log(error))
