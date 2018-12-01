import React, { Component } from 'react';

export default class ListGroup extends Component {

    constructor(props){
        super(props);
    }

    render(){
        return (
            <ul className="list-group list-group-flush">    
                {this.props.listItems}
            </ul>
        );
    }
}