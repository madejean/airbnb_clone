import { Map, fromJS } from 'immutable';

import {
  STATE_FETCH_COMPLETED,
} from '../Constants/StateConstants.js';

export default function state(state = new Map(), action = '') {
  console.log('reducer called with state as map()', new Map(), 'and action', action)
  switch (action.type) {
    case STATE_FETCH_COMPLETED:
      return state.merge(action.entities.states);
    default:
      return state;
  }
}
