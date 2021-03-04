function q1() {
    $('#SNL-strInstructions').empty();
    $('#SNL-strDrink').empty();
    $('#test1').empty();
    // $('#names-q1').empty();

    $.ajax({
        type: "GET",
        url: "https://www.thecocktaildb.com/api/json/v1/1/random.php",
        data: {},
        success: function (response) {
            console.log(response)
            const data = response['drinks'][0]
            let SNLimgurl = data['strDrinkThumb'];
            $("#SNL-strDrinkThumb").attr("src", SNLimgurl);

            let SNLstrInstructions = data['strInstructions'];
            temp_SNLstrInstructions = `<h5>${SNLstrInstructions}</h5>`
            $("#SNL-strInstructions").append(temp_SNLstrInstructions);

            let SNLstrDrink = data['strDrink'];
            temp_SNLstrDrink = `<h1>${SNLstrDrink}</h1>`
            $("#SNL-strDrink").append(temp_SNLstrDrink);

            for (let i = 1; i <= 15; i++) {
                let measures = 'strMeasure' + i;
                let ingredients = 'strIngredient' + i;
                if (data[measures] != null && data[ingredients] != null) {
                    let temp_list = `<li>${data[ingredients]} : ${data[measures]}<li>`;
                    console.log(temp_list)
                    $("#test1").append(temp_list);
                }
            }
        }
    })
}