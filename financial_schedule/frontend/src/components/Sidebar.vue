<template>
  <b-sidebar id="sidebar-no-header" aria-labelledby="sidebar-no-header-title" width="150px" shadow 
        no-close-on-route-change 
        no-close-on-esc
        no-header-close
        visible
        >
    <template>
      <div class="p-3">
        <nav class="mb-3">
          <b-nav vertical>
            <b-nav-item active @click="view_all">View All</b-nav-item>
            <b-nav-item href="#" @click="view_bills">Bills</b-nav-item>
            <b-nav-item href="#" @click="view_invoices">Invoices</b-nav-item>
            <b-nav-item href="#" @click="view_quote">Quote</b-nav-item>
            <b-nav-item href="#" @click="view_porder">Purchase Order</b-nav-item>
            <!-- <b-button v-b-toggle.sidebar-no-header>Toggle Sidebar</b-button> -->
          </b-nav>
        </nav>
      </div>
    </template>
  </b-sidebar>
</template>

<script>
export default {
    methods: {
        view_all() {
            console.log("view all");
            return ""
        },
        view_bills() {
            console.log("view bills");
        },
        view_invoices() {
            console.log("view invoices");
        },
        view_quote() {  
            console.log("view quote");
        },
        view_porder() {
            console.log("view purchase order");
        }
    }
}
</script>

<style>

</style>
