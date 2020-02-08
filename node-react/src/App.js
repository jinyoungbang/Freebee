import React, { Component } from 'react'
import GoogleMapReact from 'google-map-react';
import Maps from './Maps'

const AnyReactComponent = ({ text }) => <div>{text}</div>;

class App extends Component {
  render() {
    return (
      <div className="container">
        <Maps />
      </div>
    )
  }
}

export default App