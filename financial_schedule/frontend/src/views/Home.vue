<template>
  <div class="home">
    
    Home: Log in page

  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Navbar from "@/components/Navbar.vue"; // @ is an alias to /src

@Options({
  components: {
    
  },
})
export default class Home extends Vue {}
</script>
