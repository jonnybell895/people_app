import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";


const Table = ({ data }) =>
  !data.length ? (<p>Nothing to show</p>) : (
    <div className="column">
      <h4 className="subtitle">
        Showing <strong>{data.length} items</strong>
      </h4>
      <table className="table is-striped">
        <thead>
          <tr>
            <th>Marked</th>
            {Object.entries(data[0]).map(el => <th key={key(el)}>{el[0].charAt(0).toUpperCase() + el[0].slice(1)}</th>)}
          </tr>
        </thead>
        <tbody>
          {data.map(el => (
            <tr key={el.id}>
              <td><input type="checkbox" id={el.id} /></td>
              {Object.entries(el).map(el => <td key={key(el)}>{el[1]}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

Table.propTypes = {
  data: PropTypes.array.isRequired
};

export default Table;