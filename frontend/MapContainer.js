import React from 'react';
import { MapContainer as LeafletMap, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const NTUST_CENTER = [25.0132, 121.5418];

function MapContainer({ buildings, unlockedIds }) {
  return (
    <LeafletMap center={NTUST_CENTER} zoom={17} style={{ width: '100%', height: '400px' }}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
        url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
      />
      {buildings.map(b => (
        <Marker
          key={b.id}
          position={[b.latitude, b.longitude]}
          // 標記顏色可進階用自訂 icon
        >
          <Popup>
            <strong>{b.name}</strong><br />
            {b.description}<br />
            解鎖點數：{b.points_required}<br />
            {unlockedIds.includes(b.id) ? <span style={{color:'green'}}>已解鎖</span> : <span style={{color:'red'}}>未解鎖</span>}
          </Popup>
        </Marker>
      ))}
    </LeafletMap>
  );
}

export default MapContainer;