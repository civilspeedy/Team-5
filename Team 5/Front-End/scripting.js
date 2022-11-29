let products = [{
    name: "Lamp",
 price: 59.99,
 quantity: 10,
 image: "Images/lamp.jpg"},
{name: "desk",
price: 120.99,
quantity: 5,
image: "desk.png"
}]; //can't get json reading working yet so this is test data for now

/**This function will fill the page with products from datastore */
function populate(){    
    let pageProducts = "";
    var productDisplay = document.getElementById("productDisplay");
    for (let product in products){
        var productData = products[product];
        pageProducts += "<div class='product'><img src=" + productData.image + "><br>\n<p class='productName'>" + productData.name + "</p><br>\n<p class='productPrice'>" + productData.price + "</p></div>";
    }
    productDisplay.innerHTML = pageProducts;
}

/**This function is meant to fetch a json file */
function getfile(filename){
    fetch("./Back-End/json/products.json")
        .then((response) => response.json())
        .then((json) => console.log(json));
}

populate();