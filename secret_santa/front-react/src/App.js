import React, { Component, Fragment } from "react";
import Header from "./components/Boxes/Header";
import Home from "./components/Home";

class App extends Component {

  render() {
    return (
      <Fragment>
        <Header />
        <Home />
      </Fragment>
    );
  }
}

export default App;