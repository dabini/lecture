<template>
    <div>
        <h2>Lunch</h2>
        <!-- <p>{{ menus }}</p> -->
        <button @click="pick">랜덤선택</button>
        <p>{{ choice }}</p>
    </div>
</template>

<script>
import _ from 'lodash'

export default {
    data : function() {
        return {
            menus : ['짜장면', '짬뽕', '김밥', '돈까스', '피자', '라면', '제육볶음'],
            choice: ''
        }
    },
    methods : {
        pick : function() {
            this.choice = _.sample(this.menus)
        }
    }

}
</script>

<style>
    
</style>