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

    var url = 'http://localhost:8000/save-worklog/'
    var emails = document.getElementById('email').value
    var calls = document.getElementById('call').value
    var hours = document.getElementById('hour').value
	var meetings = document.getElementById('meeting').value
	var breaks = document.getElementById('break').value
	let today = new Date().toISOString().slice(0, 10)

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
				'date': today,
				'emails': emails,
				'calls': calls,
				'hours': hours,
				'meetings': meetings,
				'breaks': breaks,
			})
		}).then(function(response){
			alert('Your worklog for this week has been saved')
			//window.location.replace('http://localhost:8000/dashboard')

			//get user preferences

			 async function getPreferences() {
				const response = await fetch('http://localhost:8000/user-preferences/');
				return response.json();
			}

			getPreferences().then((data) => {
				var flagurl = 'http://localhost:8000/flag-user/'
				var pref_emails = data['0'].emails
			    var pref_calls = data['0'].calls
			    var pref_hrs = data['0'].hours
			    var pref_meetings = data['0'].meetings
			    var pref_breaks = data['0'].breaks

			//compare them to entered information to see if there is any that need flagging

				if (emails != pref_emails) {
					fetch(flagurl, {
						method: 'POST',
						headers:{
							'Content-type' : 'application/json',
							'X-CSRFToken' : csrftoken
						},
						body:JSON.stringify({
							'user': user,
							'date_flagged': today,
							'flag': 'Email Count',
							'preference': pref_emails,
							'work_done': emails,
						})

					}) 
				}

				if (calls != pref_calls) {
					fetch(flagurl, {
						method: 'POST',
						headers:{
							'Content-type' : 'application/json',
							'X-CSRFToken' : csrftoken
						},
						body:JSON.stringify({
							'user': user,
							'date_flagged': today,
							'flag': 'Call Amount',
							'preference': pref_calls,
							'work_done': calls,
						})

					}) 
				}

				if (hours != pref_hrs) {
					fetch(flagurl, {
						method: 'POST',
						headers:{
							'Content-type' : 'application/json',
							'X-CSRFToken' : csrftoken
						},
						body:JSON.stringify({
							'user': user,
							'date_flagged': today,
							'flag': 'Hours Worked',
							'preference': pref_hrs,
							'work_done': hours,
						})

					}) 
				}

				if (meetings != pref_meetings) {
					fetch(flagurl, {
						method: 'POST',
						headers:{
							'Content-type' : 'application/json',
							'X-CSRFToken' : csrftoken
						},
						body:JSON.stringify({
							'user': user,
							'date_flagged': today,
							'flag': 'Meetings Attended',
							'preference': pref_meetings,
							'work_done': meetings,
						})

					}) 

				}

				if (breaks != pref_breaks) {
					fetch(flagurl, {
						method: 'POST',
						headers:{
							'Content-type' : 'application/json',
							'X-CSRFToken' : csrftoken
						},
						body:JSON.stringify({
							'user': user,
							'date_flagged': today,
							'flag': 'Breaks Taken',
							'preference': pref_breaks,
							'work_done': breaks,
						})

					}) 

				}

			}) 

		}) 


	}
});
});