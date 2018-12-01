import React, { Component } from 'react';

export default class Card extends Component {
    constructor(props){
        super(props);
    }
    render(){
        return (
            <div className="card mt-5">
                <div className="card-body">
                    <h3 className="card-title">{this.props.title}</h3>
                    {this.props.content}
                </div>
            </div>
        );
    }

}