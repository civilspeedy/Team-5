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
    fs.readFile(jsonFile, 'utf8', function readFileCallback(error, tempData){
        if (error){
            console.log(error);
        } else {
        tempObj = JSON.parse(tempData); 
        tempObj.table.push(data); 
        json = JSON.stringify(tmepObj); 
        fs.writeFile(jsonFile, json, 'utf8', callback); 
    }});

}

//**Encrypts and returns data */
function encryption(data){
    var encryptedData = SubtleCrypto.encryption()
}

/**Generates encryption key.
 * Reference:https://docs.w3cub.com/dom/subtlecrypto/generatekey
*/
function generateKey(){
    let keyPair = SubtleCrypto.generateKey(
        {
            name: "RSA-OAEP",
            modulusLengthm,
            publicExponent: new Uint8Array([1, 0, 1]),
            hash:"SHA-256"
        },
            true,
            ["encrypt", "decrypt"]
    );
}