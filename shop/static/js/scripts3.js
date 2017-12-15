var map, infoWindow, locale;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 12
  });
  infoWindow = new google.maps.InfoWindow;

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      locale = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      console.log(locale.lat)
      console.log(locale.lng)
      
      infoWindow.setPosition(locale);
      infoWindow.setContent('Location found.');
      infoWindow.open(map);
      map.setCenter(locale);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(locale);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}
$('button').click(function(event){
    event.preventDefault()
    form = $("form")
    qwerty={'lat':locale.lat,'lng':locale.lng}
    $.ajax({
      'url':'/ajax/setup/',
      'type':'POST',
      'data':qwerty,
      'dataType':'json',
      'success': function(data){
        console.log(locale)
        alert(data['success'])
      },
    })
  })