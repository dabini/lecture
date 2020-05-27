<template>
  <div>
      <h1>Lotto</h1>
      <button @click="getLotto">숫자 생성</button>
      <p>{{ myNumbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name : 'Lotto',
    data : function() {
        return {
            numbers : _.range(1, 46),
            myNumbers : ''
        }
    },
    methods : {
        getLotto : function() {
            this.myNumbers = _.sampleSize(this.numbers, 6)
            this.myNumbers.sort((x, y) => x-y)
        }
    }
}
</script>

<style>

</style>