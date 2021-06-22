<template>
  <div class="home">
    <Navbar/>
    <Sidebar/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import Sidebar from "@/components/Sidebar.vue"

export default {
  name: "Home",
  components: {
    Navbar, Sidebar
  },
};
</script>
