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

$(document).ready( function () {

    var table = $('#table').DataTable({
    	"pageLength": 5,
    		"lengthMenu": [ [5, 10, 20, -1], [5, 10, 20, "All"] ],
    	ajax: {
    		url: 'http://localhost:8000/flagged-list/',
    		dataSrc: ''
    },
    	columns: [
    		{data : 'user'},
    		{data : 'date_flagged'},
    		{data : 'flag'},
            {data : 'preference'},
            {data : 'work_done'},
            {data : 'id'},
            {data : 'action_taken'},
    		{ 'data': null, title: 'Toggle', wrap: true, width:"180px", "render": function (item) { 
    			return `<a class="btn-group" >
    				 <button type="button" class="btn btn-info">Toggle Action Taken</button>` }
    	 },
    	]

    }); 

    $('#table tbody').on( 'click', 'button', function () {
        var flag = table.row( $(this).parents('tr') ).data();
        window.location.replace(`http://localhost:8000/edit-flag/${flag.id}`)
    });
});