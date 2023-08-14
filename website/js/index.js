document.getElementById('noJSWarningMessage').remove();

function redirectTo(url) {
    window.location.href = url;
}
function raiseError(error) {
    alert(`An error has occured.\nThe website may no longer be functional.` +
    `\nPlease reload the page. If the error persists, contact the website creator.` +
    `\nError: ${error}`);
}

// fetch().then(res => {

// }).catch(err => {
//     raiseError(err);
// });

console.log("Loaded");