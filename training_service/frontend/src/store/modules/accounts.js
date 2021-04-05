import { Accounts } from '../../api/accounts'
import { SET_AUTH_USER, GET_GROUPS, SET_ERRORS, GET_USER, GET_PARTICIPATIONS } from '../mutation-types'

const state = {
  jwt: localStorage.getItem('token'),
  groups: [],
  errors: [],
  authUser: {},
  participations: []
}

const getters = {
  isAuth: state => !!state.jwt
}

const mutations = {
  [SET_AUTH_USER] (state, data) {
    localStorage.setItem('token', data.access)
  },
  [GET_GROUPS] (state, groups) {
    state.groups = groups
  },
  [SET_ERRORS] (state, errors) {
    state.errors = errors
  },
  [GET_USER] (state, user) {
    state.authUser = user
  },
  [GET_PARTICIPATIONS] (state, participations) {
    state.participations = participations
  }
}

const actions = {
  login ({ commit }, data) {
    return Accounts.authUser(data).then(response => commit(SET_AUTH_USER, response.data))
  },
  createUser ({commit}, data) {
    return Accounts.create(data)
  },
  updateUser ({commit}, {user, data}) {
    let config = {
      headers: {
        'Authorization': 'Bearer '.concat(state.jwt)
      }
    }
    return Accounts.update(user, data, config)
  },
  getGroups ({commit}) {
    return Accounts.getGroups().then(response => commit(GET_GROUPS, response.data))
  },
  setErrors ({commit}, errors) {
    let errorsData = []
    for (let key in errors.response.data) {
      errors.response.data[key].forEach(element => {
        errorsData = [element, ...errorsData]
      })
    }
    commit(SET_ERRORS, errorsData)
  },
  getUser ({commit}, token) {
    let config = {
      headers: {
        'Authorization': 'Bearer '.concat(state.jwt)
      }
    }
    return Accounts.getUser(token, config).then(response => commit(GET_USER, response.data))
  },
  getParticipations ({commit}, user) {
    let config = {
      headers: {
        'Authorization': 'Bearer '.concat(state.jwt)
      }
    }
    return Accounts.getParticipations(user, config).then(response => commit(GET_PARTICIPATIONS, response.data))
  }
}

export default{
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
