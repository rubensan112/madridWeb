<template>
<div>
  <h1>You are in component Home. Router works?</h1>
  <hello-component name="Pass Home.vue of frontendv3" />

  <router-link to="/test">Go to Test </router-link>
    <router-link to="/">Go to Home</router-link>

  </div>
</template>

<script>

import HelloComponent from './HelloComponent.vue'

export default {
  components: {
    HelloComponent,
  },
}

</script>