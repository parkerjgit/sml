<template>
  <div id="app">
    <main-header></main-header>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/Header'
export default {
  name: 'App',
  components: {
    'main-header': Header
  }
}
</script>

<style>
#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
  font-family: "Space Mono", Icons /*!Google*/;
  letter-spacing: .1rem;
  font-style: normal;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  padding: 0;
  margin: 0;
}
</style>
