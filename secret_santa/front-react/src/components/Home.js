import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import BoxesList from "./Boxes/BoxesList";
import NewBoxesModal from "./Boxes/NewBoxesModal";

import axios from "axios";

import { API_URL_BOXES } from "../constants";

class Home extends Component {
  state = {
    boxes: []
  };

  componentDidMount() {
    this.resetState();
  }

  getBoxes = () => {
    axios.get(API_URL_BOXES).then(res => this.setState({ boxes: res.data }));
  };

  resetState = () => {
    this.getBoxes();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <BoxesList
              boxes={this.state.boxes}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewBoxesModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;