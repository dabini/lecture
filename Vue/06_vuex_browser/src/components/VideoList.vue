<template>
    <ul class="list-group col-lg-4">
        <videoListItem 
        @video-select="onVideoSelect"
        :video="video" 
        v-for="video in $store.state.videos" 
        :key="video.etag"
        />
    </ul>
</template>

<script>
import VideoListItem from "./VideoListItem.vue"
import { mapState } from "vuex"

export default {
    name: "VideoList",
    components: {
        VideoListItem,
    },
    data() {
        return {
            ...mapState(['videos'])
        }
    }

}
</script>

<style>

</style>