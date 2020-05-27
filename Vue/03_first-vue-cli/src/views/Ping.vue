<template>
  <div>
      <h1>Ping</h1>
      <input type="text" v-model="inputText" @keyup.enter="sendToPong">
  </div>
</template>

<script>
export default {
    name: "Ping",
    data: function() {
        return {
            inputText: '',
        }
    },
    methods : {
        sendToPong : function(){
            // this.$router.push(`/pong?message=${this.inputText}`)
            this.$router.push({name : 'Pong', query: { message:this.inputText } })
        }
    }
}
</script>

<style>

</style>