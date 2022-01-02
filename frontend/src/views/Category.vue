<template>
  <div class="home container fadein" >

      <div class="row transp-white">
        <div class="col s12 m7 nopad">
        <img src="/imgs/port3.jpg" class="img-resp nopad fadein">
      </div>
      <div class="col s12 m4 content black-text bold-text" >
        <h3>GREETINGS FROM MylXyloto Art Gallery</h3>
        <p>We have diverse artworks waiting for you to explore. 
        Check out our collections and find that quality artwork you've been searching for.</p>
        <a class="waves-effect waves-light btn-large grey darken-1" >View Our Collections</a>
      </div>
  </div>

  </div>
</template>

<script>

  export default {
    name: 'Home',
    }
</script>

<style scoped>
    img {
      width: 100%;
      max-height: 78vh;
    }

    @media only screen and (max-width: 601px){
      img {
        height: 50vh;
        max-height: 78vh;
      }

      .content{
      height: 26vh;
      }
      .transp-white {
       min-height: 55em;
       margin-top: 2.5em;
      }
    }
    .content{
      min-height: 26vh;
      font-size: 20px;
    }

    .p {
    font-weight: 250;
    }
</style>