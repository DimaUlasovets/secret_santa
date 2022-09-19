import React, { Component } from "react";
import { Table } from "reactstrap";
import NewGiftRequestModal from "./NewGiftRequestModal";
import ConfirmRemovalModal from "./ConfirmRemovalModal";

class GiftRequestList extends Component {

  render() {
    const giftrequests = this.props.giftrequests;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>User</th>
            <th>Gift</th>
            <th>Box</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!giftrequests || giftrequests.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            giftrequests.map(gift => (
              <tr key={gift}>
                <td>{gift.user.email}</td>
                <td>{gift.description}</td>
                <td>{gift.box.name_box}</td>
                <td align="center">
                  <NewGiftRequestModal
                    create={false}
                    gift={gift}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    id={gift.id}
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

export default GiftRequestList;
