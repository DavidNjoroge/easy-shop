var map, infoWindow;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 12
  });
  infoWindow = new google.maps.InfoWindow;

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      infoWindow.setPosition(pos);
      infoWindow.setContent('Location found.');
      infoWindow.open(map);
      map.setCenter(pos);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}
qwerty={'get':'working'}
$.ajax({
    'url':'/ajax/all_shops/',
    'type':'GET',
    'success':function(data){
        for (i=0;i<data.length;i++){
            console.log(data[i].latitude)
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(data[i].latitude, data[i].longitude),
                map: map,
                title:data[i].shopname,
                url: "shop/"+data[i].id
            });
            google.maps.event.addListener(marker, 'click', function() {
                window.location.href = this.url;
            });
        }
    }
})  