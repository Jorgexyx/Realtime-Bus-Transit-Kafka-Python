import React, {useState, Fragment } from 'react';
import logo from './logo.svg';
import './App.css';
import { Map, Marker, Popup, TileLayer } from 'react-leaflet'


const LeafletMap = () => {
  const [markers, setMarkers]  = useState({})

  const source = new EventSource('/api/transit'); //ENTER YOUR TOPICNAME HERE
  source.addEventListener('message', (e) => {
    const { route_id, longitude, latitude } = JSON.parse(e.data)
    console.log(longitude, latitude)
    setMarkers((prev) => ({
      ...prev, 
      [route_id]: {longitude, latitude}
    }))
  }, false);

  const position = [-118.2801742, 34.1643375]
  return(
    <Map center={position} zoom={13}>
      <TileLayer
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url='https://{s}.tile.osm.org/{z}/{x}/{y}.png'
      />

      {Object.entries(markers).map( ([route_id, {longitude, latitude}]) => 
          <Marker id={route_id} position={[longitude, latitude]}>
            <Popup>A pretty CSS3 popup.<br />Easily customizable.</Popup>
          </Marker>
      )}

    </Map>
  )

}

const Header = () => {
  return(
    <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Real Time L.A. Metro Transit Maps
        </p>
    </header>
  )
}

function App() {

  return (
    <Fragment>
      <Header />
      <LeafletMap />
    </Fragment>
  );
}

export default App;
