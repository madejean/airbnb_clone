import { connect } from 'react-redux';
//bindActionCreators produce hash action creators already bound to dispatch
import { bindActionCreators } from 'redux';
//
import { Map } from 'immutable';

import {
  fetchStates,
} from '../Actions/StatesActionCreators.js';

import component from './StatesSelector.js';

export function mapStateToProps(state) {
  return {
    states: state.StatesReducer,
  };
}

export function mapDispatchToProps(dispatch) {
  return bindActionCreators({
    fetchStates,
  }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(component);
