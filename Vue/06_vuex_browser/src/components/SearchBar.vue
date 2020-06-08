<template>
  <div class="search-bar">
      <input @keypress.enter="onInput">
  </div>
</template>

<script>
export default {
    name: "SearchBar",
    methods : {
        onInput(event) {
            this.$emit('input-change', event.target.value)
        }
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