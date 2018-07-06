import React, { Component } from 'react';

export default class Container extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return ( 
            <div className="container"> 
                <h1 className="text-info">{this.props.title}</h1>
                {this.props.content}
            </div>
        );
    }
}