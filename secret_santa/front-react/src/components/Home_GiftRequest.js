import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import GiftRequestList from "./GiftRequestList";
import NewGiftRequestModal from "./NewGiftRequestModal";

import axios from "axios";

import { API_URL_GIFT_REQUEST } from "../constants";

class Home_GiftRequest extends Component {
  state = {
    giftrequests: []
  };

  componentDidMount() {
    this.resetState();
  }

  getGiftRequest = () => {
    axios.get(API_URL_GIFT_REQUEST).then(res => this.setState({ giftrequests: res.data }));
    console.log(this.state.giftrequests)
  };

  resetState = () => {
    this.getGiftRequest();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <GiftRequestList
              giftrequests={this.state.giftrequests}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewGiftRequestModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home_GiftRequest;
