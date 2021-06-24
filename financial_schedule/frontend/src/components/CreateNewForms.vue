<template>
  <div>
    <template v-if="this.type == 'bills'">
      Create Bills
    </template>

    <template v-if="this.type == 'invoices'">
      Create Invoices
    </template>

    <template v-if="this.type == 'quote'">
      Create Quote
    </template>

    <template v-if="this.type == 'purchae_order'">
      Create Purchase Order
    </template>

    <template v-else>
      Something wrong
    </template>
  </div>
</template>

<script>
export default {
  name: "CreateNewForms",
  props: {
    type: String
  },
  data() {
    return {
    }
  },
}
</script>