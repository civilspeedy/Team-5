function getAllProducts(){
    let request = new XMLHttpRequest();
    var package = "/api/getAllProducts"

    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            var productArray = JSON.parse(this.responseText)[2];
            var insert = ""//Injecting HTML
            var count = 0;

            for (const product of productArray){
                count++;
                console.log(product);
                insert += "<div class='grid-item' id='product"+count+"'>"+product[0]+"<br>\n<img src='static/images/"+product[3]+"'>\n<p>£"+product[1]+"</p>\n<button class='basketBtn' href='#'>View</button>\n</div>";
            }
            return document.getElementById("products").innerHTML = insert;
        }
        else if (this.status == 400){
            console.log("failure");
        }
    }
    request.open('GET', package, true);
    request.send();


}

/**function to get the variables from the search bar and set it to a js variable called searchTerm for later use -charliek*/
function getSearchTerm(){
    var searchTerm = document.getElementById("searchBox").value;
    let request = new XMLHttpRequest();
    var package = "/api/getSearchTerm?term=" + searchTerm;


    request.onreadystatechange = function(){
        var insert = "";
        var count = 0;
    
        if (this.readyState == 4 && this.status == 200){
            var productArray = JSON.parse(this.responseText)[2];
            for (const product of productArray){
                count++;
                insert += "<div class='grid-item' id='product"+count+"'>"+product[0]+"<br>\n<img src='static/images/"+product[3]+"'\n<p>£"+product[1]+"</p>\n<button class='basketBtn' href='#'>View</button>\n</div>";
            }
            return document.getElementById("results").innerHTML = insert;
        }
        if (this.status == 400){    
            console.log(JSON.parse(this.responseText));
        }
    }
    request.open('GET', package, true);
    request.send();
}

function getFeatured(){
    let request = new XMLHttpRequest();
    var package = "/api/getFeatured";
    var count = 0;

    request.onreadystatechange = function(){
        var insert = "";

        if (this.readyState == 4 && this.status == 200){
            var productArray = JSON.parse(this.responseText)[2];
            for (const product of productArray){
                count++;
                insert += "<div class='grid-item' id='product"+count+"'>"+product[0]+"<br>\n<img src='static/images/"+product[3]+"'\n<p>£"+product[1]+"</p>\n<button class='basketBtn' href='#'>View</button>\n</div>";
            }
            return document.getElementById("products").innerHTML = insert;
        }
        if (this.status == 400){    
            console.log(JSON.parse(this.responseText));
        }
    }
    request.open('GET', package, true);
    request.send();
}


function signUp(){
    let request = new XMLHttpRequest();
    var package = "/api/signUp?username=" + document.getElementById("username").value + "&password=" +document.getElementById("password").value
    
    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            alert("Sign Up Successful")
        }
        else if (this.status == 400){
            alert("Sign Up Failed")
        }
    }
    request.open('GET', package, true);
    request.send();
}

function login(){
    
    var usernameVar = document.getElementById("usernameBox").value;
    var passwordVar = document.getElementById("passwordBox").value;

    let request = new XMLHttpRequest();
    var package = "api/login?username=" + usernameVar + "&password=" + passwordVar

    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            alert("You are logged in");
        }
        if (this.status = 400){
            alert("Incorrect Login")
        }
    }

    request.open('GET', package, true);
    request.send();
}

