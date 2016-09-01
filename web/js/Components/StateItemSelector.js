import React from 'react';
import ReactDOM from 'react-dom';

class Item extends React.Component {
  constructor(props){
    super();
    this.state = {
      checked: false
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick (e) {
    this.setState({
      checked: !this.state.checked
    });
  }
  render() {
    let text = this.state.checked?
    <bold>{this.props.states}</bold> : this.props.states;
    return (
          <div className="rows">
          <br />
            <input type="checkbox" onClick={this.handleClick} /> {text}
          </div>
    );
  }
}
let data = [<Item states="California" />, <Item states="Arizona" />, <Item states="Nevada" />, <Item states="Louisiana" />];

class StateList extends React.Component {
  constructor(props){
    super();
  }
  render (){
    let items = data.map(thing => thing);
    var styles = {
        list: {
          padding: '30px',
        }
    }
    return (
      <div style={styles.list}>
        <h1>States</h1> 
        <h2>{items}</h2>
      </div>
    );
  }
}

export default StateList;
