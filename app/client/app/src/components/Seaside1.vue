<template>
<div class="grid">

  <div class="a"><img src="../assets/images/seaside_artspace/96dpi/open-seaside-96dpi.jpg"></img></div>
  <div class="b">10</div>
  <div class="c">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fringilla est ullamcorper eget nulla facilisi etiam. Lorem sed risus ultricies tristique nulla aliquet enim. Nisl vel pretium lectus quam id leo in vitae turpis. Libero enim sed faucibus turpis. Mus mauris vitae ultricies leo. Orci eu lobortis elementum nibh tellus molestie nunc non.
    </p>
  </div>
  <div class="d">
    <p>2016</p>
    <p>
      ----------------------------------
      ----------------------------------
      ----------------------------------
    </p>
    <p>
      Project Scope: Architectural Design
      Roles: Senior Architect, Computational designer
      Collabortors: OPEN Architecture, Li Hu, Wenjing Huange
      Client: Tianxingjiuzhou Real Estate Development Co.
      Status: under construction
    </p>
  </div>
  <div class="e">
    <div>DUNE Artspace</div>
  </div>
  <div class="f">
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
  align-items:center;
  grid-template-columns: repeat(24, 1fr);
  grid-template-rows: repeat(12, 1fr);
  height:100vh;
}
.cell {
  border: dotted 1px lightgrey;
}
.a { grid-area: 1 / 1 / 13 / 25; }
.b { grid-area: 7 / 1; font-size: 2.5em;}
.c { grid-area: 7 / 4 / 10 / 12; column-count: 2; font-size: 80%}
.d { grid-area: 2 / 16 / 5 / 19;}
.e { grid-area: 8 / 14 / 11 / 20; align-self: center; font-size: 400%; }
.f { grid-area: 11 / 16 / 12 / 19;}

@include wide {
  .grid {
    display: inherit;
  }
}

</style>
