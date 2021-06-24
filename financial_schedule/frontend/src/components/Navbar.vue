<template>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">Logo</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <b-nav-item-dropdown text="Lang" right>
                    <template #button-content>
                        <em> Plus Sign </em>
                    </template>
                    Create new
                    <b-dropdown-item @click="create_new('bills')"> Bills </b-dropdown-item>
                    <b-dropdown-item @click="create_new('invoices')">Invoices</b-dropdown-item>
                    <b-dropdown-item @click="create_new('quote')">Quote</b-dropdown-item>
                    <b-dropdown-item @click="create_new('purchae_order')">Purchase Order</b-dropdown-item>
                </b-nav-item-dropdown>

                <b-nav-item-dropdown right>
                    <!-- Using 'button-content' slot -->
                    <template #button-content>
                        <em>User</em>
                    </template>
                    <b-dropdown-item>Profile</b-dropdown-item>
                    <b-dropdown-item href="#">Sign Out</b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    navigate_to_generate(link) {
        window.location.href = link;
    },
    create_new(type){
        this.$router.push({
            name: 'create-new-forms',
            param: { type: type }
        })
    }
  }
};
</script>