import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default new Vuex.Store({
  state: {
    inputValue: '',
    videos: [],
    selectedVideo: null, 
  },
  getters: {
    videoUrl(state) {
      return `https://www.youtube.com/embed/${state.selectedVideo.id.videoId}`
    },
    videoTitle(state) {
      return state.selectedVideo.snippet.title
    },
    videoDescription: state => state.selectedVideo.snippet.description

  },
  mutations: {
    setInputValue(state, inputValue){
      state.inputValue = inputValue
    },
    setVideos(state, videos) {
      state.videos = videos
    },
    setSelectedVideo(state, video) {
      console.log("MUTATION", state)
      state.selectedVideo = video
    },
  },
  actions: {
    fetchVideos({commit, state}, event) {
      context.commit('setInputValue', event.target.value)
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: state.inputValue,
        }
      })
        .then(res => {
          res.data.items.forEach(item => {
            const parser = new DOMParser()
            const doc = parser.parseFromString(item.snippet.title, 'text/html')
            item.snippet.title = doc.body.innerText
          })
          commit('setVideos', res.data.items)
        })
        .catch(err => console.error(err))
    }
  },
  modules: {
  }
})
