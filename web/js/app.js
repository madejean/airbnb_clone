import React from 'react';
import ReactDOM from 'react-dom';

import StatesReducer from './Reducers/states.js';

import {
  applyMiddleware,
  combineReducers,
  createStore,
} from 'redux';

import {
  Provider,
} from 'react-redux';

import thunk from 'redux-thunk';

const store = createStore(
  combineReducers({ StatesReducer }),
  applyMiddleware(thunk)
);

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
