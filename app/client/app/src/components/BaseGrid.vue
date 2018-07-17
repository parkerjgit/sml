<template>
<div class="grid">
  <div v-for="_ in (num_rows * num_cols)" class="cell"></div>
</div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      num_rows: 24,
      num_cols: 12
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.grid {
  display: grid;
  grid-template-columns: repeat(24, 1fr);
  grid-template-rows: repeat(12, 1fr);
  height:100vh;
}
.cell {
  border: dotted 1px lightgrey;
}
</style>
