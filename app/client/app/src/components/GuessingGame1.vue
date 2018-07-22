<template>
<div class="grid">

  <div class="a"></div> <!-- <img src="../assets/images/guessing_game/screenshots.jpg"></img> -->
  <div class="b">
    <span>The Guessing Game</span>
  </div>
  <div class="c">
    <p>
      Top Left: Cell sizing diagram
      Spread: Photo of 3d-printed model.
      images courtesy of OPEN Architecture
    </p>
  </div>

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

<!-- Page-scoped styling -->
<style lang="scss" scoped>
@import '../assets/scss/style';
.grid {
  display: grid;
  // align-items:center;
  grid-template-columns: repeat(24, 1fr);
  grid-template-rows: repeat(12, 1fr);
  height:100vh;
}
.cell {
  border: dotted 1px lightgrey;
}
.a { grid-area: 5 / 13 / 13 / 25;  background: whitesmoke; }
.b { grid-area: 5 / 1 / 6 / 11; font-size: 2.5em; text-align: right;}
.c { grid-area: 7 / 3 / 10 / 11; font-size: 80%; text-align: right;}
.d { grid-area: 2 / 16 / 5 / 19;}
.e { grid-area: 8 / 14 / 11 / 20; align-self: center; font-size: 400%; }
.f { grid-area: 11 / 16 / 12 / 19;}

// @include wide {
//   .grid {
//     display: inherit;
//   }

// }

</style>
