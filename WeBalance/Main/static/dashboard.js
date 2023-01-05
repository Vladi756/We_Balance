$(document).ready( function () {

var email_count, call_count, hours_count, meetings_count, breaks_count;

async function fetchData(){
    const response = await fetch('http://localhost:8000/user-workdone/');
    const data = await response.json();

    function getThisWeeksWorkDone() {
        let x = new Date(Math.max.apply(null, data.map(function(e) {
        return new Date(e.date);
    })));
    var recent = data.filter(function(d){
    return d.date === x;
    });
    console.log(recent[0])
    document.getElementById("test").innerHTML = recent;
    }

    data.forEach(obj => {
        Object.entries(obj).forEach(([key,value]) => {
            if (key = 'emails') {
                
            }
        }

            ) 
    })
}
});