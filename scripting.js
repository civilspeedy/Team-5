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
        var productData = products[product]; //I'm not sure why but the for in loop is only returning the location value of the objects so this is a temporary fix
        var name = productData.name.toString
        pageProducts += "<div class='product'><img src=" + productData.image + "><br>\n<p class='productName'>" + productData.name + "</p><br>\n<p class='productPrice'>£" + productData.price + "</p><br>\n<button name='product button' onclick='addToBasket("+name+")'>Add to Basket</button></div>";
    }
    productDisplay.innerHTML = pageProducts;
}

/**This function is meant to fetch a json file */
function getfile(){
    fetch("../Back-End/json/products.json")
        .then((response) => response.json())
        .then((json) => console.log(json));
}
/**this function will eventually add items to the basket but at the moment the function causes an error stating there is a loose } at line 2 of index.html */
function addToBasket(selectedProduct){
    console.log(selectedProduct);
}

populate();
getfile();