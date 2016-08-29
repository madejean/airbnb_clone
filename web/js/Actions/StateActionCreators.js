//ajax API request
import request from 'superagent';

//Normalizr takes JSON and a schema and replaces nested entities with their IDs, gathering all entities in dictionaries.
//="normalize"

import {
  arrayOf,
  normalize,
  Schema,
} from 'normalizr';

import {
  STATE_FETCH_COMPLETED,
  STATE_FETCH_ERROR,
  STATE_FETCH_INITIATED,
} from '../Constants/StateConstants.js';

const state = new Schema('states', {
  idAttribute: 'id',
});

export function fetchStatesInitiated() {
  return {
    type: STATE_FETCH_INITIATED,
  };
}

export function fetchStatesErrored(error) {
  return {
    type: STATE_FETCH_ERROR,
    error,
  };
}

export function fetchStatesCompleted(response) {
  return Object.assign({
    type: STATE_FETCH_COMPLETED,
  }, normalize(response.states, arrayOf(state)));
}

export function fetchStates() {
  return dispatch => {
    dispatch(fetchStatesInitiated());

//superagent ajax API request
    request.get('/./states.json')
      .then((data) => {
        dispatch(fetchStatesCompleted(data.body));
      }).catch((error) => {
        dispatch(fetchStatesErrored(error));
      });
  };
}
