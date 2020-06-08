<template>
  <div class="container">
    <SearchBar />
    <div class="row">
      <VideoDetail/>
      <VideoList />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from "./components/SearchBar.vue"
import VideoList from  "./components/VideoList.vue"
import VideoDetail from  "./components/VideoDetail.vue"

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
    }
  }

</script>

<style scoped>
  /* div {
    border: 3px solid black;
    padding: 3px;
    margin: 3px;
  } */
</style>
