<template>

<div class="grid">

  <!-- <div class="grid-cell" style="text-align:left; font-size: 32px; font-weight: bold;">
    001
  </div> -->

  <div class="grid-cell" v-for="_ in num_items">
    <div class="subgrid">

      <div class="cell"
      v-for="_ in pickRand(num_digits)"
      v-bind:style="{
        'grid-column': pickRand(subgrid_col),
        'grid-row': pickRand(subgrid_row) }">
        {{ digits[pickRandId(digits)] }}
      </div>

      <div class="thumb"
      v-bind:style="{
        'grid-column-start': 3,
        'grid-column-end': 9,
        'grid-row-start': 2,
        'grid-row-end': 5
      }">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0d0IuaLLH9xvU3BwBi6GfV6yRE0bHDoVr2hpRUrRhsul5dsSkqA" width="42" height="42"></img>
      </div>

    </div>
  </div>
</div>

</template>

<script>
// import VideojsRecorderPlayer from './VideojsRecorderPlayer'

export default {
  name: 'Home',
  data () {
    return {
      num_items: 100,
      digits: [1,2,3,4,5,6,8,7,9],
      digit: 0,
      num_digits: [0,1,2,4,8,16,32],
      subgrid_row: [1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3],
      subgrid_col: [1,1,2,2,3,4]
    }
  },
  methods: {
    pickRand: function(arr) {
      return arr[Math.floor(Math.random() * arr.length)];
    },
    pickRandId: function(arr) {
      return Math.floor(Math.random() * arr.length);
    },
    time: function() {
      // var self = this
      this.shuffle(this.digits)
      // this.digit = this.pickRand(this.digits)
      setInterval(this.time, 200)
    },
    shuffle: function(arr) {
      for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }
      return arr;
    }
  },
  mounted() {
    // this.time()
  },
  components: {
    // 'videojs-recoder-player': VideojsRecorderPlayer
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*,
*:before,
*:after {
  box-sizing: border-box;
}

.grid {
  display: grid;
  margin: 0 auto;
   grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-template-columns: repeat(auto-fill, 200px);
   /* grid-auto-rows: minmax(200px, auto); */
  /*grid-auto-rows: auto;*/
}

.grid-cell {
  /* needed for the flex layout*/
  /*margin: 2px;*/
  /*flex: 1 1 200px;*/
  border: dotted 1px whitesmoke;

}

.subgrid {
  display: grid;
/*   margin: 20px; */
/*   grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); */
  grid-template-columns: repeat(13, 1fr);
  grid-auto-rows: minmax(0px, auto);
  /* grid-auto-rows: repeat(2, 1fr); */
}

.cell {
  /* border: solid 1px whitesmoke; */
  background-color: transparent;
  background: rgba(255,0,0,.3);

  color: white;
  grid-column: 3;
  font-size: 32px;
  /*font-weight: bold;*/
  line-height: .9em;
}

.thumb {
  background: blue;
}

.header {
  grid-column: -1;
  grid-row: 1;
}

.footer {
  /*flex: 0 1 100%;*/
  grid-column: 1 / -1;
}

.grid > * {
  /*background-color: #444;
  color: #fff;*/
  /*border: solid 1px white;*/
  /*padding: 10px;*/
  /*font-size: 150%;
  margin-bottom: 10px;*/
}


/* We need to set the margin used on flex items to 0 as we have gaps in grid.  */

/*@supports (display: grid) {
  .wrapper > * {
    margin: 0;
  }
}*/
</style>
