<template>
  <div class="search-bar">
      <input @keypress.enter="fetchVideos">
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default { 
    name: "SearchBar",
    methods : {
        ...mapActions([
            'fetchVideos'
        ])
    }
}
</script>

<style>
    div.search-bar {
        text-align: center;
        margin: 20px;
    }

    div.search-bar > input {
        width: 75%;
    }
</style>