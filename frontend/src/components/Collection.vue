<template>
        <div class="col m4 show-on-med-and-up">
          <div class="card" @click="go(collection)" @mouseover="pulse='pulsar'" @mouseleave="pulse=''" :class="pulse">
            <div class="card-image">
              <img :src="url">
            </div>
            <div class="card-content black-text">
              {{title}}
            </div>
         </div>
        </div>
      <div class="hide-on-med-and-up">
      </div>
</template>

<script>
export default {
  name: 'CollectionSel',
  props: {
    url: String,
    title: String,
    collection: String,
  },
  methods: {
    go: function(coll="") {
      this.$router.push({name: 'Collection', params:{ "collection": coll}});
    }
  },
  data: function() {
    return {pulse: ""}
  }
}
</script>

<style scoped>

.card-content {
  padding: 5px;
  font-weight: bolder;
}

img {
  max-height: 11em !important;
  object-fit: cover !important;
  object-position: center !important;
}
</style>
