<template>
  <div>
    <h2>Lotto</h2>
    <button @click="getLotto">랜덤선택</button>
    <p>{{ lottoNumber }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    data : function() {
        return {
            numbers : _.range(1, 46),
            lottoNumber : '',
        }
    },
    methods : {
        getLotto() {
            this.lottoNumber = _.sampleSize(this.numbers, 6)
            this.lottoNumber.sort((a, b) => a-b)
        }
    }
}
</script>

<style>

</style>