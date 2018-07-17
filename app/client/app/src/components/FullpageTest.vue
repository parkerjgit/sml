<template>
  <div>
    <full-page :options="options">
      <div class="section">
        First section ...
      </div>
      <seaside></seaside>
    </full-page>
  </div>
</template>

<script>
import FullPage from '../../node_modules/vue-fullpage.js/src/FullPage'
import Seaside from './Seaside'

export default {
  components: {
    FullPage,
    'seaside': Seaside,
  },

  data() {
    return {
      options: {
        css3: false,
        scrollingSpeed: 700,
        autoScrolling: false,
        fitToSection: false,
        // fitToSectionDelay: 1000,
        scrollBar: false,
        easing: 'easeInOutCubic',
        easingcss3: 'ease',
        loopBottom: false,
        loopTop: false,
        loopHorizontal: true,
        continuousVertical: false,
        continuousHorizontal: false,
        scrollHorizontally: false,
        interlockedSlides: false,
        dragAndMove: false,
        offsetSections: false,
        resetSliders: false,
        fadingEffect: false,
        normalScrollElements: '#element1, .element2',
        scrollOverflow: true,
        scrollOverflowOptions: null,
        touchSensitivity: 15,
        normalScrollElementTouchThreshold: 5,
        bigSectionsDestination: null,
      },
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
