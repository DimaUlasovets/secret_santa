import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL_BOXES } from "src/constants";

class NewBoxesForm extends React.Component {

    
    state = {
        id: 0,
        name_box: "",
        end_date: null
      };

      componentDidMount() {
        if (this.props.box) {
          const {id, name_box, end_date} = this.props.box;
          this.setState({id, name_box, end_date});
        }
      }
    
      onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
      };
    
      createBox = e => {
        e.preventDefault();
        axios.post(API_URL_BOXES, this.state).then(() => {
          this.props.resetState();
          this.props.toggle();
        });
      };
    
      editBox = e => {
        e.preventDefault();
        axios.patch(API_URL_BOXES + this.state.id, this.state.name_box, this.state.end_date).then(() => {
          this.props.resetState();
          this.props.toggle();
        });
      };

    
      defaultIfEmpty = value => {
        return value === "" ? "" : value;
      };
      
      handleChange = (field, e) => {
        this.setState({ [field]: e.target.value });
      };
    
      render() {
        return (
          <Form onSubmit={this.props.box ? this.editBox : this.createBox}>
            <FormGroup>
              <Label for="name_box">Name:</Label>
              <Input
                type="text"
                name="name_box"
                onChange={this.onChange}
                value={this.defaultIfEmpty(this.state.name_box)}
              />
            </FormGroup>

            <FormGroup >
              <Label for="end_date">End Date:</Label>
              <input
                type="datetime-local"
                value={this.state.datetime}
                onChange={e => this.handleChange("end_date", e)}
              />
   
            </FormGroup>

            <Button>Send</Button>
          </Form>
        );
      }
}

export default NewBoxesForm;