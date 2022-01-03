<template>
  <div class="hide-on-med-and-up"><br></div>
  <div class="container fadein" >
  <div style="margin-right: 0.35em" class="right black-text" @click="showsearch = !showsearch">X</div>
  <h5 class="black-text"  @click="showsearch = !showsearch">Search</h5>
  <div class="row" v-show="showsearch">
    <form class="col s12 bold-text">
      <div class="row">
        <div class="input-field col s6">
          <input id="search" type="text" class="validate" name="s">
          <label for="search">Search</label>
        </div>
        <a class="btn" @click="clickPage(1)">Search</a>
        <div class="input-field col s12 m7">
        <span class="black-text">Sort By: </span>
        <p>
      <label>
        <input name="sort" type="radio" value="alpha" checked />
        <span>Alphabet</span>
      </label>
    </p>
    <p>
      <label>
        <input name="sort" type="radio" value="collection"/>
        <span>Category</span>
      </label>
    </p>
    <p>
      <label>
        <input class="with-gap" name="sort" type="radio" value="created" />
        <span>Created</span>
      </label>
    </p>
    <p>
      <label>
        <input name="sort" type="radio" value="artist" />
        <span>Artist</span>
      </label>
    </p>
       </div>
       <div class="input-field col s12 m5">
        <span class="black-text">Order: </span>
        <p>
      <label>
        <input name="asc_desc" value="asc" type="radio" checked />
        <span>Ascending</span>
      </label>
    </p>
    <p>
      <label>
        <input name="asc_desc" type="radio" value="desc" />
        <span>Descending</span>
      </label>
    </p>
    </div>
    <div class="input-field col s12">
<!--   <select name="coll">
      <option value="all">Collection</option>
      <option value="1">Option 1</option>
      <option value="2">Option 2</option>
      <option value="3">Option 3</option>
    </select>-->
  </div>

      </div>
    </form>
  </div>
  </div>

  <div class="container fadein" style="margin-top:-1em">
    <h4 class="black-text center">Collection</h4>
    <div class="">
      <div id="collection" class="black-text">
      </div>
      <center>
        <ul class="row">
          <li class="waves-effect black"><a @click="clickPage(page-1)" ><i class="material-icons">chevron_left</i></a></li>
          <li style="margin-left: 1em" class="waves-effect black"><a @click="clickPage(page+1)" ><i class="material-icons">chevron_right</i></a></li>
        </ul>
        <span class="black-text">page {{page}}</span>
      </center>
    </div>
    <div></div>
  </div>
</template>

<script>

  export default {
    name: 'Collection',
    data: function() {
        return {
          showsearch: false,
          collectionHTML: "",
          page: 1,
          backendurl: window.location.origin + "/collections"
        }
      },
    mounted: function() {
      var elems = document.querySelectorAll('select');
      window.M.FormSelect.init(elems);
      this.clickPage(this.page);
    },
    methods: {
      clickPage: function(page=0){
        var m, url;
        var urlparam = {s: 0, p: '', order_by: '', coll: '', asc_desc: ''};
        if (page < 1){
          m = new URLSearchParams(window.location.search);
          page = 1;
        }
        else {
          m = new URLSearchParams(new FormData(document.getElementsByTagName('form')[0]));
        }
        this.page = page;
        urlparam["s"] = m.get('s');
        urlparam["p"] = page;
        urlparam["order_by"] = m.get('sort');
        if (this.$route.params.collection){
          urlparam["coll"] = this.$route.params.collection;
        }
        urlparam["asc_desc"] = m.get('asc_desc');
        var param = new URLSearchParams(urlparam)
        url = this.backendurl + "?" + param.toString();
        this.fetchCollection(url);
      },
      fetchCollection: function(url) {
                          document.getElementById("collection").innerHTML = `<div class="progress"><div class="indeterminate"></div></div>`;
                          fetch(url).then(response => {
                            response.text().then((text) => {
                              this.collectionHTML = text;
                              document.getElementById("collection").innerHTML = text;
                            })
                          });
                        }
              }
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
    .container{
      padding: 0.4em;
      margin-top: 0.4em;
      margin-bottom: 1.5em;
      background-color: #fffffff4;
    }

    .card-content, .card-title {
      color: black !important;
      font-weight: bolder !important;
    }

    h5 {
      margin-top: 6px;
      margin-top: 6px;
    }

    p {
      display: inline !important;
    }

    .pagination li {
      background-color: #817071 !important;
    }
    
</style>
