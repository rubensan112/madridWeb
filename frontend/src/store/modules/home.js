
//import {doApiCall} from '../../client'
import axios from "axios";

const state = {
    count: 0,
    infApi: {
        total: 0,
        example : 0,
        example2 : 0,
        example3 : 0
    }
  };

const actions = {
  getApiCall(context) {
      //let url = 'http://127.0.0.1:8000/tutorial/snippets.json';
    //return doApiCall('GET', url)
        console.log("API call to http://127.0.0.1:8000/api/ChangeManagement/ChangeRequest.json") //Esta llamada se produce bien
        axios
      .get('http://127.0.0.1:8000/api/ChangeManagement/ChangeRequest.json')
      .then(response => {
        if (response.status === 200) {
          context.commit('setApiCall', response.data) //Llamada a la mutacion setApiCall
        }


      });
        console.log("API call finish") //Esta llamada se produce bien
  },
};

const mutations = {
    increment (state) {
      state.count++
    },
    setApiCall (state, reportData) {
      state.infApi = Object.assign({}, state.infApi, //Cambia las variables.
          {
          total: reportData['count'],
              example : reportData['count'],
              example2 : reportData['results'][0]['description'],
              example3 : reportData['results'][0]['description'],
      }
      )
    }
  };


export default {
  state,
  mutations,
  actions
}