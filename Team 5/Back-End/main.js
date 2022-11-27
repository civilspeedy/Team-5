const { callbackify } = require('util');

function getLogin(choice){
    if (choice = "username"){
        var username = document.getElementById("username");
        return username
    }
    if (choice = "password"){
        var password = document.getElementById("password");
        return password
    }
}

/**this function will take an input and store it within chosen json file */
function writeToJson(jsonFile, data){
    var tempObj = {
        hold: []
    };


}
console.log(generateKey());