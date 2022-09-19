import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import {useLocation} from 'react-router-dom';
import axios from "axios";

import { API_URL_GIFT_REQUEST } from "../constants/index";

class NewGiftRequestForm extends React.Component {

    state = {
        id: 0,
        user: "",
        description: "",
        box: ""
      };

      componentDidMount() {
        if (this.props.giftrequest) {
          const {id, user, description, box} = this.props.giftrequest;
          this.setState({id, user, description, box});
          console.log(this.props.location.box_list_data)
        }
      }

      onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
      };

      createGiftRequest = e => {
        e.preventDefault();
        axios.post(API_URL_GIFT_REQUEST, this.state).then(() => {
          this.props.resetState();
          this.props.toggle();
        });
      };

      editGiftRequest = e => {
        e.preventDefault();
        axios.patch(API_URL_GIFT_REQUEST + this.state.id, this.state.user, this.state.description).then(() => {
          this.props.resetState();
          this.props.toggle();
        });
      };


      defaultIfEmpty = value => {
        return value === "" ? "" : value;
      };

      handleChange = (field, e) => {
        const location = useLocation();
        this.setState({ [field]: location.state.data });
      };

      render() {
        return (
          <Form onSubmit={this.props.giftrequest ? this.editGiftRequest : this.createGiftRequest}>
            <FormGroup>
              <Label for="description">Box-id:</Label>
              <Input
                type="text"
                name="description"
                defaultValue={e => this.handleChange("box", e)}
              />
            </FormGroup>

            <FormGroup>
              <Label for="user">User-Email:</Label>
              <Input
                type="text"
                name="user"
                onChange={this.onChange}
                value={this.defaultIfEmpty(this.state.user)}
              />
            </FormGroup>

            <FormGroup>
              <Label for="description">Description-Gift:</Label>
              <Input
                type="text"
                name="description"
                onChange={this.onChange}
                value={this.defaultIfEmpty(this.state.description)}
              />
            </FormGroup>

            <Button>Send</Button>
          </Form>
        );
      }
}

export default NewGiftRequestForm;
