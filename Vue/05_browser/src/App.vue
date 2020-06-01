<template>
  <div class="container">
    <SearchBar @input-change="onInputChange"/>
    <VideoList :videos="videos" />
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from "./components/SearchBar.vue"
import VideoList from  "./components/VideoList.vue"

const API_KEY = "AIzaSyBGbJ5rXX0PXq98f0fCLq8DKmUxyPqCGsA"
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
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

<style>
</style>
