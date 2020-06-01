<template>
  <div class="parent">
      <h1>부모 컴포넌트</h1>
      <Child @hugry="parentMsg = '밥먹어라' " :propFromParent="parentMsg"/>
  </div>
</template>

<script>
import Child from '../components/Child.vue'

export default {
    name: 'Parent',
    data() {
        return {
            parentMsg : '부모에서 내리는 메세지',
        }
    },
}
</script>

<style>
    .parent {
        border: 3px solid red;
        margin: 3px;
        padding: 3px;
    }
</style>