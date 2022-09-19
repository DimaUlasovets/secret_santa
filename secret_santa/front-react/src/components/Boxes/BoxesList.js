import React, { Component } from "react";
import { Table } from "reactstrap";
import NewBoxesModal from "./NewBoxesModal";
import { useNavigate, Link } from 'react-router-dom';
import ConfirmRemovalModal from "../ConfirmRemovalModal";


const handleOnClick = (boxid) => {

  const navigate = useNavigate();
  navigate('/giftrequest', {state:{data:boxid}});
  console.log('Send message!');
};

class BoxesList extends Component {

  render() {
    const boxes = this.props.boxes;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name_box</th>
            <th>Created date</th>
            <th>End Date</th>
            <th>Status Box</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!boxes || boxes.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            boxes.map(box => (
              <tr key={box} onClick={e => handleOnClick(box.id)}>
                <td>{box.name_box}</td>
                <td>{box.create_date}</td>
                <td>{box.end_date}</td>
                <td>{box.status_box}</td>
                <td align="center">
                  <NewBoxesModal
                    create={false}
                    box={box}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    id={box.id}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default BoxesList;