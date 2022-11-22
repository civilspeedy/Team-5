const { callbackify } = require('util');

function getLogin(){
    var password = document.getElementById("password");
    var username = document.getElementById("username");
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