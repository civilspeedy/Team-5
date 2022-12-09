function getAllProducts(){
    let request = new XMLHttpRequest();
    var package = "/api/getAllProducts"

    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            console.log(JSON.parse(this.responseText));
        }
        else{
            console.log("failure")
        }
    }
}

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
    request.open('GET', package, true);
    request.send();
}

function login(){
    
    var usernameVar = document.getElementById("usernameBox").value;
    var passwordVar = document.getElementById("passwordBox").value;
    console.log(usernameVar,"has been set to js variable 'username'");
    console.log(passwordVar,"has been set to js variable 'password'");
}

function getSearchTerm(){
    searchItem = document.getElementById('searchBox').value;//gets what the user has entered into search box

    let request = new XMLHttpRequest();
    var package = "/api/getSearchTerm?term=" + searchItem;
    
    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            console.log(JSON.parse(this.responseText));
        }
        else if (this.status == 400){
            console.log("Failure");
        }
    }
    request.open('GET', package, true);
    request.send();
}