<template>
  <div class="home">
    <Navbar/>
    <Sidebar/>
    <Calendar/>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import Sidebar from "@/components/Sidebar.vue";
import Calendar from "@/components/Calendar.vue";

export default {
  name: "Home",
  components: {
    Navbar, 
    Sidebar,
    Calendar
  },
};
</script>
