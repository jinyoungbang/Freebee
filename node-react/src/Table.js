import React, { Component } from 'react'

class Table extends Component {
  render() {
    return (
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Job</th>
            <th>Flavor</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Charlie</td>
            <td>Janitor</td>
            <td>Taro</td>
          </tr>
          <tr>
            <td>Mac</td>
            <td>Bouncer</td>
            <td>Mango</td>
          </tr>
          <tr>
            <td>Dee</td>
            <td>Aspiring actress</td>
            <td>Milk</td>
          </tr>
          <tr>
            <td>Dennis</td>
            <td>Bartender</td>
            <td>Passion Fruit</td>
          </tr>
        </tbody>
      </table>
    )
  }
}

export default Table