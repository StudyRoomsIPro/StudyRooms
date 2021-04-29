// jQuery 3.x-style ready event and locally scoped $
/*
jQuery(function($) {
    $('html').removeClass('nojs');
    $('html').addClass('hasjs');
  });
  
  // Creating an object based off of the users input
$(document).ready(function(){
  var people = [], // Creating 'people' object array
    $ins = $('#first_name, #last_name, #studentID, #email_address'),
    counter = {
      first_name: {},
      last_name: {},
      studentID: {},
	    email_address: {}
    };
	
// Creating jQuery function for submission 
  $('#submit').click(function() {
    var person = {},
      valid = true;
    $ins.each(function() {
      var val = this.value.trim();
      if (val) {
        person[this.id] = val;
      }
    }); // If submission is valid, add a 'person' object to the 'people' array
    if (valid) {
      people.push(person);
      $ins.val('');

      // Adding a count to the 'people' array
      $.each(person, function(key, value) {
        var count = counter[key][value] || 0;
        counter[key][value] = count + 1;
      });
    }
	
	// Creating jQuery function to display the data, and stringify
	// the JS object into a JSON string
    $('#display_user').click(function() {
    $('p').text(JSON.stringify(people) );
    })
    })
  });
*/
function reserve() {
	var begin = document.cookie.split('; ').find(row => row.startsWith('startTime=')).split('=')[1];
	var end = document.cookie.split('; ').find(row => row.startsWith('endTime=')).split('=')[1];
	var roomName = document.cookie.split('; ').find(row => row.startsWith('roomName1=')).split('=')[1];

	document.getElementById("foo").innerHTML = begin + " " + end + " " + roomName;
	location.href = {{ url_for("confirmed", beginTime=begin, endTime=end, room=roomName) }};
}
