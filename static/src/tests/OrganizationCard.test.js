import React from 'react';
import ReactDOM from 'react-dom';
import { shallow } from 'enzyme'
import OrganizationCard from '../components/OrganizationCard';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<OrganizationCard />, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('checks to see if title is present', ()=>{
    const wrapper = shallow(<OrganizationCard />)
    const textTitle =<h3 className="card-title">Organization</h3>
    expect(wrapper.contains(textTitle)).toEqual(true)
})
