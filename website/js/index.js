document.getElementById('noJSWarningMessage').remove();
const revealSecretMessageButton = document.getElementById("revealSecretMessage");
const secretMessageElement = document.getElementById('secretMessage');
const apiURL = 'http://127.0.0.1:5000/secretMessage';

function redirectTo(url) {
    window.location.href = url;
}
function raiseError(error) {
    alert(`An error has occured.\nThe website may no longer be functional.` +
    `\nPlease reload the page. If the error persists, contact the website creator.` +
    `\nError: ${error}`);
}
function fetchSecretMessage() {
    fetch(apiURL).then(async res => {
        responseText = await res.text();
        secretMessageElement.outerText = responseText;
    }).catch(err => raiseError(err));
}

revealSecretMessageButton.onclick = fetchSecretMessage;

console.log("Loaded");