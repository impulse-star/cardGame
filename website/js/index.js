document.getElementById('noJSWarningMessage').remove();

function raiseError(error) {
    alert(`An error has occured.\nThe website may no longer be functional.\nError: ${error}`);
}

// fetch().then(res => {

// }).catch(err => {
//     raiseError(err);
// });

console.log("Loaded");