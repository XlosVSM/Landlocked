// Initialize the map
const map = L.map('map').setView([-41.2865, 174.7762], 12); // Wellington coordinates

// Add OSM tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Load GeoJSON data and add white polygons
fetch('../data/Wellington.geojson')
    .then(response => response.json())
    .then(data => {
        console.log('GeoJSON loaded:', data);
        L.geoJSON(data, {
            style: { color: 'white', weight: 2, fillColor: 'white', fillOpacity: 1 }
        }).addTo(map);
    })
    .catch(err => console.error('Error loading GeoJSON:', err));
