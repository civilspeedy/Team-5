let products = [{
    name: "Lamp",
    price: 59.99,
    quantity: 10,
    image: "../Images/lamp.jpg"},
{
    name: "desk",
    price: 120.99,
    quantity: 5,
    image: "desk.png"}]; //can't get json reading working yet so this is test data for now

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


/**function to get the variables from the search bar and set it to a js variable called searchTerm for later use -charliek*/
function getSearchTerm(){
    var searchTerm = document.getElementById("searchBox").value;
    console.log(searchTerm," has been set to js variable 'searchTerm'" );
}

function signUp(){
    let request = new XMLHttpRequest();
    var package = "/api/signUp?username=" + document.getElementById("username").value + "&password=" +document.getElementById("password").value
    
    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            console.log(JSON.parse(this.responseText));
        }
        console.log(JSON.parse(this.responseText));
    }
    request.open('POST', package, true);
}
