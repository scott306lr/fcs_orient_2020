<template>
  <div class="about">
    <h3>This page will include introduction and rules.</h3>
  </div>
</template>

<script>
export default {
  name: "About",
  components: {},
  //data() {},
  created() {
    this.group_id = this.$route.query.group;
  },
  methods: {},
};
</script>
