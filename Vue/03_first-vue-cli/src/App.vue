<template>
  <div id="app">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <MyComponent />
    <GreatComponent />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComponent from './components/MyComponent.vue'
import GreatComponent from './components/GreatComponent.vue'


export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent,
    GreatComponent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
