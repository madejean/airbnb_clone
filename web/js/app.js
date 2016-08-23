import React from 'react';
import ReactDOM from 'react-dom';

import Header from './Components/Header.js';
import Sidebar from './Components/LeftColumn.js';
import Footer from './Components/Footer.js';
import Content from './Components/Content.js';

ReactDOM.render(
  (
    <div>
      <Header />
      <Sidebar />
      <Footer />
      <Content />
    </div>
  ),
document.getElementById('main')
);
