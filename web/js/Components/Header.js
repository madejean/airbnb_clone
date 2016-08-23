import React from 'react';

class Header extends React.Component {
  render() {
    var borderColor = '#e6e3e3';
    var styles = {
      header : {
        borderRadius: '3px',
        border: '1px solid ' + borderColor,
        height: '60px',
        marginLeft: '10px',
        padding: '0px 10px 0px 10px',
      },
      div : {
        width: '200px',
        height: '60px',
        float: 'right',
        background: '#D3D3D3',
      },
      logo : {
        position: 'absolute',
        left: '20px',
        top: '15px',
        padding: '0px 10px 0px 10px',
      },

  };

return (
  <div style={styles.header}>
  <div style={styles.div}>
  <img src={"https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_Bélo.svg/1280px-Airbnb_Logo_Bélo.svg.png"} width={150} style={styles.logo}/>
  </div>
  </div>
)
 /*const Header = (props) => (
  <div style={styles.header}>
    <img src={props.imageUrl} width={150} />
  </div>
);*/
  }
}
/*
Header.propTypes = {
  imageUrl: React.PropTypes.string,
};

Header.defaultProps = {
  imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_Bélo.svg/1280px-Airbnb_Logo_Bélo.svg.png"
};*/

export default Header;
