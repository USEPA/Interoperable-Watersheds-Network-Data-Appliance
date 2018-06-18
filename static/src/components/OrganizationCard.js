import React, { Component } from 'react';

export default class OrganizationCard extends Component {
    constructor(props){
        super(props)
    }
    render(){
        const orgId = this.props.orgData ? this.props.orgData.orgId : ''
        const orgName = this.props.orgData ? this.props.orgData.orgName : ''
        const orgSubId  = this.props.orgData ? this.props.orgData.orgSubId : ''
        const orgUrl  = this.props.orgData ? this.props.orgData.orgUrl : ''
        const contactName = this.props.orgData ? this.props.orgData.contactName : ''
        const contactEmail = this.props.orgData ? this.props.orgData.contactEmail : ''
        console.log(orgId)
        console.log(this.props.orgData)
        return (
            <div className="card mt-5">
                <div className="card-body">
                    <h3 className="card-title">Organization</h3>
                    <ul className="list-group list-group-flush">
                        <li className="list-group-item bg-light">
                            <div className="row">
                                <div className="col-md-4 text-info">
                                    <b>Organization Identifier:</b>
                                </div>
                                <div className="col-md-8">
                                    {orgId}
                                </div>
                            </div>
                        </li>
                        <li className="list-group-item">
                            <div className="row">
                                <div className="col-md-4 text-info">
                                    <b>Organization Name:</b>
                                </div>
                                <div className="col-md-8">
                                    {orgName}
                                </div>
                            </div>
                        </li>
                        <li className="list-group-item bg-light">
                            <div className="row">
                                <div className="col-md-4 text-info">
                                    <b>Organization Subpart Identifier:</b>
                                </div>
                                <div className="col-md-8">
                                    {orgSubId}
                                </div>
                            </div>
                        </li>
                        <li className="list-group-item">
                            <div className="row">
                                <div className="col-md-4 text-info">
                                    <b>Organization URL:</b>
                                </div>
                                <div className="col-md-8">
                                    {orgUrl}
                                </div>
                            </div>
                        </li>
                        <li className="list-group-item bg-light">
                            <div className="row">
                                <div className="col-md-4 text-info">
                                    <b>Contact Name:</b>
                                </div>
                                <div className="col-md-8">
                                    {contactName}
                                </div>
                            </div>
                        </li>
                        <li className="list-group-item">
                            <div className="row">
                                <div className="col-md-4 text-info">
                                    <b>Contact Email:</b>
                                </div>
                                <div className="col-md-8">
                                    {contactEmail}
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        )
    }

}