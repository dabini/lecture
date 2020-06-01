<template>
  <div>
      <h1>VideoList</h1>
      <ul>
          <li v-for="video in videos" :key="video.etag">
              <img :src="video.snippet.thumbnails.default.url">
              <p>{{ video.snippet.description  }}</p>
          </li>
      </ul>
  </div>
</template>

<script>
export default {
    name: "VideoList",
    props: {
        videos: Array,
    }

}
</script>

<style>

</style>