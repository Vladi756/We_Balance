$(function(){

	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie !== '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = cookies[i].trim();
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) === (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
		}

var csrftoken = getCookie('csrftoken');

var form = document.getElementById('myForm')
form.addEventListener('submit', function(e){
    e.preventDefault()

    var url = 'http://localhost:8000/save-preferences/'
    var emails = document.getElementById('email').value
    var calls = document.getElementById('call').value
    var hours = document.getElementById('hour').value
	var meetings = document.getElementById('meeting').value
	var breaks = document.getElementById('break').value

	if (emails === '') {
		alert("Please select the amount of emails you'd like to send")
	}
	else if (calls === '') {
		alert("Please select the amount of calls you'd like to take")
	}
	else if (hours === '') {
		alert("Please select the amount of hours you'd like to work")
	}
	else if (meetings === '') {
		alert("Please select the amount of meetings you'd like to attend")
	}
	else if (breaks === '') {
		alert("Please select the amount of breaks you'd like to take")
	}
	else{
		fetch(url, {
			method: 'POST',
			headers:{
				'Content-type' : 'application/json',
				'X-CSRFToken' : csrftoken
			},
			body:JSON.stringify({
				'user': user,
				'emails': emails,
				'calls': calls,
				'hours': hours,
				'meetings': meetings,
				'breaks': breaks,
			})
		}).then(function(response){
			alert('Your preferences have been saved')
			window.location.replace('http://localhost:8000/dashboard')
		})
	}
});
});