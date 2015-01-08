var center = [55.679208653509434, 12.562839388847351];
var prosa = [55.6790271772563, 12.562839388847351];
var map = L.map('map').setView(center, 16);

L.tileLayer('http://{s}.tiles.mapbox.com/v3/jchillerup.kmm460oi/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18
}).addTo(map);

var marker = L.marker(prosa).addTo(map);
marker.bindPopup("Cryptoparty København").openPopup();
