import React from 'react';

class Sidebar extends React.Component {
  render() {
    var borderColor = '#e6e3e3';
    var styles = {
      sidebar : {
          border: '1px solid ' + borderColor,
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
          width: '300px',
          marginLeft: '10px',
          background: '#e6e6e6',
          padding: '10px',
          height: '100%',
        }
      }

   return (
        <div style={styles.sidebar}>
          </div>
    );
  }
}
  /*const sidebar = (props) => (
  <div style={styles.sidebar}>
  </div>
);*/
export default Sidebar;
