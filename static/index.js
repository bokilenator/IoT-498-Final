var newShoe = 'slippers';

$(function(){

	$(document).ready(function(){
		var elems = document.querySelectorAll('.modal');
		options = {
			onOpenStart: function() {
				console.log('starting stream');
				$("#replaceStream").html("<img class='col s8 center offset-s2' src='/video_feed'></img>");
			}
		};
    	var instances = M.Modal.init(elems, options);
	  });

	$('#capture').click(function(){
		console.log('capture called')
		doAjax('/capture/' + newShoe);
		$.ajax({
			url: '/capture/',
			type: 'GET',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});

	$('#recommend').click(function(){
		$.ajax({
			url: 'http://api.openweathermap.org/data/2.5/weather?q=Seattle&units=imperial&appid=be398bfb5752a6b5ad4c17f15544034a',
			type: 'GET',
			success: function(response){
                produceRec(response.main.temp, response.weather[0].description, response.weather[0].id);
				console.log(response);
                console.log(response.main.feels_like)
			},
			error: function(error){
				console.log(error);
			}
		});
	});

	$('#lit-slippers').click(function(){
		doAjax('/slippers');
	})
	$('#lit-sneakers').click(function(){
		doAjax('/sneakers');
	})
	$('#lit-snowboots').click(function(){
		doAjax('/snowboots');
	})
	$('#lit-rainboots').click(function(){
		doAjax('/rainboots');
	});

	$('#replace-slippers').click(function(){
		newShoe = 'slippers';
	});
	$('#replace-sneakers').click(function(){
		newShoe = 'sneakers';
	});
	$('#replace-snowboots').click(function(){
		newShoe = 'snowboots';
	});
	$('#replace-rainboots').click(function(){
		newShoe = 'rainboots';
	});
});

function doAjax(url) {
	$.ajax({
		url: url,
		type: 'GET',
		success: function(response){
			console.log(response);
		},
		error: function(error){
			console.log(error);
		}
	});
}

function produceRec(temperature, description, id) {
	let recommendation = 'The current temperature is ' + temperature + '°F and the weather is ' + description + '. You should wear ';
	if (temperature < 40 || (id >= 600 && id < 700)){
		recommendation = recommendation + "snow boots";
		doAjax('/snowboots');
	} else if (id >= 200 && id < 600) {
		recommendation = recommendation + "rain boots";
		doAjax('/rainboots');
	}
	else if (temperature > 75) {
		recommendation = recommendation + "slippers";
		doAjax('/slippers');
	} else {
		recommendation = recommendation + "sneakers";
		doAjax('/sneakers');
	}

	$('#recommendation').text(recommendation + ".");
}