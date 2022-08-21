import React, { Component, Fragment } from "react";
import Header from "./components/Boxes/Header";
import Home_GiftRequest from "./components/GiftRecuest/Home_GiftRequest";

class App_GiftRequest extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Home_GiftRequest />
      </Fragment>
    );
  }
}

export default App_GiftRequest;