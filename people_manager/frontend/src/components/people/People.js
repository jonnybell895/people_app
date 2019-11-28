import React, { Component } from 'react';
import DataProvider from "../DataProvider";
import Table from "../layout/Table";


export class People extends Component {
  render() {
    return (
      <div>
        <h1>People List</h1>
        <DataProvider endpoint="people" render={data => <Table data={data} />} />
      </div>
    )
  }
}

export default People