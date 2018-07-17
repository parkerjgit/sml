<template>
  <div class="section">
  	<div class="slide"><seaside1></seaside1></div>
    <div class="slide"><seaside2></seaside2></div>
  	<div class="slide"> Slide 2 </div>
  	<div class="slide"> Slide 3 </div>
  	<div class="slide"> Slide 4 </div>
  </div>
</template>

<script>
import Seaside1 from './Seaside1'
import Seaside2 from './Seaside2'

export default {
  components: {
    'seaside1': Seaside1,
    'seaside2': Seaside2
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
