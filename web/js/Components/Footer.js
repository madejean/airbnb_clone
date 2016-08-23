import React from 'react';

class Footer extends React.Component {
  render() {
    var borderColor = '#e6e3e3';
    var styles = {
      footer : {
        borderRadius: '3px',
        border: '1px solid ' + borderColor,
        height: '40px',
        marginLeft: '10px',
        padding: '0px 10px 0px 10px',
        display: 'block',
        background: '#e6e6e6',
        bottom: '0px',
        }
      }

   return (
        <div style={styles.footer}>
          </div>
    );
  }
}

export default Footer;
