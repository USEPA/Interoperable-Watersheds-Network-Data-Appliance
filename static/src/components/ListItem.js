import React, { Component } from 'react';

export default class ListItem extends Component {
    constructor(props){
        super(props);
    }
    render(){
        return (
            <li className={`list-group-item ${this.props.backgroundClass}`}>
                <div className="row">
                    <div className="col-md-4 text-info">
                        <b>{this.props.label}</b>
                    </div>
                    <div className="col-md-8">
                        {this.props.dataItem}
                    </div>
                </div>
            </li>
        )
    }
}