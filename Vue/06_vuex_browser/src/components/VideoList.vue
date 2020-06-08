<template>
    <!-- <ul>
        <li v-for="video in videos" :key="video.etag">
            <img :src="video.snippet.thumbnails.default.url">
            <p>{{ video.snippet.description  }}</p>
        </li>
    </ul> -->
    <ul class="list-group col-lg-4">
        <videoListItem 
        @video-select="onVideoSelect"
        :video="video" 
        v-for="video in videos" 
        :key="video.etag"
        />
    </ul>
</template>

<script>
import VideoListItem from "./VideoListItem.vue"

export default {
    name: "VideoList",
    components: {
        VideoListItem,
    },
    props: {
        videos: Array,
    },
    methods: {
        onVideoSelect(video) {
            this.$emit('video-select', video)
        }
    }

}
</script>

<style>

</style>