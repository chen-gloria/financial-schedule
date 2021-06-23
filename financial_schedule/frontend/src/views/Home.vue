<template>
  <div class="home" style="overflow-y: scroll;">
    <Navbar/>
    <!-- If it is logged in -->
    <div class="container-fluid row">
      <div class="sidebar col-2">
        <Sidebar/>
      </div>
      <div class="main-panel col-10">
        <div class="content-wrapper text-center">
          <Calendar/>
        </div>
        <div class="footer">

        </div>
      </div>
    </div>
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
    Calendar,
  },
};
</script>
