<template>
  <div class="section">
  	<div class="slide"><guessing-game1></guessing-game1></div>
    <div class="slide"><guessing-game2></guessing-game2></div>
  </div>
</template>

<script>
import GuessingGame1 from './GuessingGame1'
import GuessingGame2 from './GuessingGame2'

export default {
  components: {
    'guessing-game1': GuessingGame1,
    'guessing-game2': GuessingGame2
  },

  data() {
    return {
      options: {
        // paddingTop: '30px'
      },
    }
  },
}
</script>

<!-- Project-Scoped Styling -->
<style scoped>
p {
  text-align: justify;
}
</style>
