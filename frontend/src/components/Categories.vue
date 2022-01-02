Collection.vue
<template>
  <div class="" id="categories">
      <div><h4 class="black-text bold center-align">Collections</h4></div>
      <div class="container">
        <div class="row">
          <CollectionSel url="/imgs/port.jpg" collection="all" title="All Collections" />
          <CollectionSel url="/imgs/art.jpg" collection="People" title="People" />
          <CollectionSel url="/imgs/homeart.jpg" collection="Abstract" title="Abstract" />
          <CollectionSel url="/imgs/2.jpg" collection="Photography" title="Photography" />
        </div>
      </div>
  </div>
</template>

<script>
import CollectionSel from '@/components/Collection.vue'
export default {
  name: 'Categories',
  components: {
    CollectionSel
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#categories {
  min-height: 5em;
  padding: 5px;

}


@media only screen and (min-width: 601px){
    #categories {
    background-color: #fafafade;
    }
  }
</style>

