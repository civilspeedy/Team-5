/**This function will fill the page with products from datastore */
function populate(){    
    let pageProducts = "";
    for (product in products){
        pageProducts += product;
    }
}

function getfile(filename){
    fetch("./Back-End/json/products.json")
        .then((response) => response.json())
        .then((json) => console.log(json))
}

function testFile(){
    console.log(products);
}

getfile("../Back-End/json/products.json")