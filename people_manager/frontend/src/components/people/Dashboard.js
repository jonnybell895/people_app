import React, { Fragment } from 'react';
import Form from './Form';
import People from './People';


export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <People />
    </Fragment>
  )
}