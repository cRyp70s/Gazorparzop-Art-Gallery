<template>
  <div class="container black-text">
    <div class="row">
      <div class="col s12 m5">
        <img :src="src" @click="go" />
      </div>
      <div class="col s12 m7">
      <h3>{{title}}</h3>
      <b>By <a href="">{{artist}}</a> | In Collection: <a @click="this.$router.push({name: 'Collection', params:{ 'collection': collection}})">{{collection}}</a> | Created: {{created}}</b>
      <br>
      <p>{{descr}}</p>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'ViewItem',
    data: function(){
      return {src: '', title: '', descr: '', artist: '', collection: '', created: ''}
    },
    methods: {
    loadFromServer: function(){
        let id = this.$route.params.id;
        let url = `http://127.0.0.1:5000/get-item/${id}`;
        fetch(url).then(response => {
            response.text().then((data) => {
              data = JSON.parse(data);
              this.src = data["img_src"];
              this.title = data["title"];
              this.descr = data["descr"];
              this.artist = data["artist"];
              this.collection = data["collection"];
              this.created = data["created"];
            })
          });
      },
      go: function() {
        window.location.href = this.src;
      }
    },
    mounted: function(){
      this.loadFromServer()
    }
  }
</script>

<style scoped>
  .container{
      padding: 0.4em;
      margin-top: 0.4em;
      margin-bottom: 1.5em;
      background-color: #ffffffd4;
      width: 85%;
    }

    img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    }
    @media only screen and (min-width: 601px){
      .container {
        max-height: 85vh;

      }

      img {
        max-height: 83vh;
      }
    }
</style>