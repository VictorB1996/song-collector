document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("submitButton").addEventListener("click", function() {
        var message = document.getElementById("message").value;
        sendMessage(message);
    });
});

function sendMessage(message) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onload = function() {
        if (xhr.status === 200) {
        } else {
            console.error("Failed to send message");
        }
    };
    xhr.send(JSON.stringify({message: message}));
    document.getElementById("message").value = "";
}
