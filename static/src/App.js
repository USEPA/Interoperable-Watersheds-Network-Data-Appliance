import React, { Component } from 'react';
import Container from './components/Container';
import Card from './components/Card';
import ListGroup from './components/ListGroup';
import ListItem from './components/ListItem';

import APIUtils from './api/APIUtils';
import Resources from './Resources.json'
import OrgsService from './services/OrgsService';

import './App.css';

export default class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            orgData: []
        }
    }

    componentDidMount() {
        let me = this;
        OrgsService.get("epar10", function(orgs) {
            me.setState({
                orgData: orgs
            });
        });
    }

    render() {
        const appTitle = Resources.appTitle;
        const orgSectionTitle = Resources.orgSectionTitle;
        const orgIdLabel = Resources.orgIdLabel;
        const orgNameLabel = Resources.orgNameLabel;
        const orgSubIdLabel = Resources.orgSubIdLabel;
        const orgUrlLabel = Resources.orgUrlLabel;
        const contactNameLabel = Resources.contactNameLabel;
        const contactEmailLabel = Resources.contactEmailLabel;
        const orgData = this.state.orgData;

        return (
          <div>
            <Container
                title={appTitle}
                content={
                    <Card 
                        title={orgSectionTitle}
                        content={
                            <ListGroup
                                listItems={
                                    [<ListItem
                                        key="li1"
                                        backgroundClass="bg-light"
                                        label={orgIdLabel}
                                        dataItem={orgData.parent_organization_id}
                                    />,
                                    <ListItem
                                        key="li2"
                                        label={orgNameLabel}
                                        dataItem={orgData.name}
                                    />,
                                    <ListItem
                                        key="li3"
                                        backgroundClass="bg-light"
                                        label={orgSubIdLabel}
                                        dataItem={orgData.organization_id}
                                    />,
                                    <ListItem
                                        key="li4"
                                        label={orgUrlLabel}
                                        dataItem={orgData.sos_url}
                                    />,
                                    <ListItem
                                        key="li5"
                                        backgroundClass="bg-light"
                                        label={contactNameLabel}
                                        dataItem={orgData.contact_name}
                                    />,
                                    <ListItem
                                        key="li6"
                                        label={contactEmailLabel}
                                        dataItem={orgData.contact_email}
                                    />]
                                }
                            />
                        }
                    />
                }
            />
          </div>
        );
    }
}

