import products from "../Back-End/json/products.json"; //json file is called


/**This function will fill the page with products from datastore */
function populate(){
    let pageProducts = "";
    for (product in products){
        pageProducts += product;
    }
}