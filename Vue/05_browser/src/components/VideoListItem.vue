<template>
  <div>
    <li @click="onVideoClick" class="video-list-item list-group-item">
      <img :src="thumbnailUrl" class="mr-3" alt="youtube-thumbnail-image">
      <div class="media-body">
        {{ video.snippet.title }}
      </div>
    </li> 
  </div>
</template>

<script>
export default {
    name: 'VideoListItem',
    props: {
      video: Object,
    },
    computed: {
      thumbnailUrl() {
        return this.video.snippet.thumbnails.default.url
      }
    },
    methods :{
      onVideoClick() {
        this.$emit('video-select', this.video)
      }
    }
}
</script>

<style scoped>
  li.video-list-item {
    display: flex;
    cursor: pointer;

  }

  li.video-list-item:hover {
    background-color: #eee;

  }

  .media-body {
    display: flex;
    flex: 1;
    
  }
</style>