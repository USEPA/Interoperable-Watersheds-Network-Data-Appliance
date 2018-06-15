import React, { Component } from 'react';
import OrganizationCard from './OrganizationCard';

const fakeServerData = {
    orgName : "Environmental Protection Agency",
    orgId : "epa",
    orgSubId : "epar10",
    orgUrl : "www.epa.gov",
    contactName : "Biscuit",
    contactEmail: "Biscuit@gravy.com"
  }
export default class Container extends Component {
    constructor(props){
        super(props)
        this.state = {}
    }

    componentDidMount(){
        this.setState({...this.state, orgData :  fakeServerData});
    }

    render(){
        return ( 
            <div className="container"> 
                <h1 className="text-info">Interoperable Watersheds Network</h1>
                <OrganizationCard orgData={this.state.orgData}/>
            </div>
        );
    }
}