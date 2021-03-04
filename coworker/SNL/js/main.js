//global variabel, get inputvalue despite of it changing 
const searchCocktail = document.getElementById('searchCocktail');

searchCocktail.addEventListener('change', () => {
    const searchValue = searchCocktail.value;
    getCocktailByName(searchValue);
})



//function with API to get random cocktail
//and calling function displayrandomCocktail to print out the cocktailinfo 
 function getrandomCocktail() {

    fetch(`https://www.thecocktaildb.com/api/json/v1/1/random.php`)
        .then((response) => response.json())
        .then((cocktailData) => {
            displayrandomCocktail(cocktailData)
        })
        .catch((error) => {
            console.log(error)
        })
}

//function with API to search cocktail by name 
//and calling function displayinputvalue to print out the cocktailinfo 
function getCocktailByName(cocktail) {
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${cocktail}`)
        .then((response) => response.json())
        .then((cocktailData) => {
            displayinputvalue(cocktailData)
        })
        .catch((error) => {
            if (document.getElementById("searchCocktail").value == "") {
                showErrMsg(error)
            } else {
                hideErrMsg(error)
            };
        })
}


//Function that creates what to display in html, called when clicking on moodButton
function displayrandomCocktail(cocktailData) {
    const { drinks } = cocktailData;
    const cocktailpictureElement = document.getElementById('cocktailPicture');
    let cocktailPicture = `
    <img class="drinkThumb" src= "${drinks[0].strDrinkThumb}">`;

    cocktailpictureElement.innerHTML = cocktailPicture;

    //display first cocktailinfo
    const cocktailTitleElement = document.getElementById('cocktailTitle');

    let cocktailInfo = `
    <h4 class="cocktailName"> ${drinks[0].strDrink} </h4>
    <p class="typeOfglass">Type of glass:</p><p>${drinks[0].strGlass}</p>
    </br><p class="howToMake">How to make:</p>`

    cocktailTitleElement.innerHTML = cocktailInfo;


    //display second cocktailinfo
    const cocktailInfoElement = document.getElementById('howTo');

    let result = '';
    for (var i = 1; i <= 15; i++) {
        let measures = 'strMeasure' + i;
        let ingridients = 'strIngredient' + i;
        if ((drinks[0][measures]) && (drinks[0][ingridients]) !== "") {
            result = result + ` <p>${drinks[0][measures]} ${drinks[0][ingridients]}</p>`;

            cocktailInfoElement.innerHTML = result;
        };
    }


    //display third cocktailinfo
    const cocktailInstructionsElement = document.getElementById('instructions');
    let instructions = `
    </br><p>${drinks[0].strInstructions}</p>`;

    cocktailInstructionsElement.innerHTML = instructions;

}


//Function that creates what to display in html
//it is being called when clicking on shakebutton to display info from input value
function displayinputvalue(cocktailData) {
    const { drinks } = cocktailData;
    const cocktailpictureElement = document.getElementById('cocktailPicture');
    let cocktailPicture = `
    <img class="drinkThumb" src= "${drinks[0].strDrinkThumb}">`;

    cocktailpictureElement.innerHTML = cocktailPicture;

    //display first cocktailinfo
    const cocktailTitleElement = document.getElementById('cocktailTitle');

    let cocktailInfo = `
    <h4 class="cocktailName"> ${drinks[0].strDrink} </h4>
    <p class="typeOfglass">Type of glass:</p><p>${drinks[0].strGlass}</p>
    </br><p class="howToMake">How to make:</p>`

    cocktailTitleElement.innerHTML = cocktailInfo;


    //display second cocktailinfo
    const cocktailInfoElement = document.getElementById('howTo');

    let result = '';
    for (var i = 1; i <= 15; i++) {
        let measures = 'strMeasure' + i;
        let ingridients = 'strIngredient' + i;
        if ((drinks[0][measures]) && (drinks[0][ingridients]) !== "") {
            result = result + ` <p>${drinks[0][measures]} ${drinks[0][ingridients]}</p>`;

            cocktailInfoElement.innerHTML = result;
        };
    }


    //display third cocktailinfo
    const cocktailInstructionsElement = document.getElementById('instructions');
    let instructions = `
    </br><p>${drinks[0].strInstructions}</p>`;

    cocktailInstructionsElement.innerHTML = instructions;

}

//Button shake
$(document).ready(function() {
    $("#shakebutton").click(function() {
        $("#shakebutton").effect("shake", { times: 3 }, 450);
    });
});


//Error to display when searchvalue is empty and shake button has been clicked

function showErrMsg(error) {
    const errorDivElement = document.getElementById('errormsg');
    const errormsg = `<p class="errormsg">You haven't told me what you want to drink.</p>`
    errorDivElement.innerHTML = errormsg;
};

function hideErrMsg(error) {
    const errorDivElement = document.getElementById('errormsg');
    errorDivElement.innerHTML = "";
};