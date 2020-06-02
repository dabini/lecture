<template>
  <div class="container">
    <SearchBar @input-change="onInputChange"/>
    <VideoList :videos="videos" />
    <VideoDetail />
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from "./components/SearchBar.vue"
import VideoList from  "./components/VideoList.vue"
import VideoDetail from  "./components/VideoDetail.vue"

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      inputValue: '',
      videos: [],
    }
  },
  methods: {
    onInputChange(inputText) {
      this.inputValue = inputText
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.inputValue,
        }
      })
        .then(res => this.videos = res.data.items)
        .catch(err => console.error(err))
    }
  },
}
</script>

<style scoped>
  /* div {
    border: 3px solid black;
    padding: 3px;
    margin: 3px;
  } */
</style>
