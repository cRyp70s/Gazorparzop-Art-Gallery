<template>
    <nav>
      <div class="nav-wrapper adv-serif-children">
        <a href="#" class="brand-logo"><img src="/imgs/logo.png" /></a>
        <div class="hide-on-med-and-up"><br></div>
        <ul id="nav-mobile" class="right left-align">
          <li class="adv-serif-children"><router-link to="/">Home</router-link></li>
          <li class="adv-serif-children" @mouseleave="showCat" @mouseover="show = true" @click="show=!show"><a>Collections</a></li>
          <li class="adv-serif-children"><router-link to="/about">About</router-link></li>
        </ul>
      </div>
    </nav>
    <categories v-show="show" @mouseleave="show = false" @click="show = false"></categories>
    <br>
    <br>

  <router-view/>
</template>

<script>
  import Categories from '@/components/Categories.vue'

  export default {
    name: 'Home',
    data: function() {
       return {
       show: false
       }
    },
    components: {
      categories: Categories
      },
    methods: {
      showCat: function(ev) {
        var el = document.getElementById("categories");
        if (el) {
          if (!((ev.clientY >= el.offsetTop) && (ev.clientY <= (el.offsetTop + el.offsetHeight)))) {
            this.show = false;
          }
        }
      }
    },
  }
</script>

<style>
  .router-link-active {
    border-bottom: 2px solid #00d0ff;
  }

  @media only screen and (min-width: 601px){
    #nav-mobile {
    margin-right: 8em;
    }
  }

  @media only screen and (max-width: 601px){
    #nav-mobile {
      float: unset !important;
    }
  }

  nav {
    background-color: unset;
    -webkit-box-shadow: unset;
    box-shadow: unset;
  
    font-weight: bold;
    padding: 1em;
  }

</style>
