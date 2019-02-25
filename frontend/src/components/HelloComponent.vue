<template>
<div>
  <h1>In HelloComponent. {{ name }}!</h1>
<h1>  {{home.count}}  </h1>
<button v-on:click="increment">Increment</button>
<h1>  {{home.infApi.total}}  </h1>
<h1>  {{home.infApi.example}}  </h1>
<h1>  {{home.infApi.example2}}  </h1>
<h1>  {{home.infApi.example3}}  </h1>
<h1>  El bundle se carga correctamente  </h1>
</div>
</template>


<script>
  import {mapState, mapMutations} from 'vuex'

export default {
  props: {
    name: {
      type: String,
      required: true
    }
  },
  computed: {
      ...mapState(['home']),
    },
   methods: {
      ...mapMutations(['increment']),
     },
   beforeMount() {
        this.$store.dispatch('getApiCall')
    }
}
</script>
