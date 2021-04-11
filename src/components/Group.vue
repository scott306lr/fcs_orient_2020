<template>
  <div>
    <b-col>
      <b-button squared variant="primary"> {{ name }} </b-button>
    </b-col>
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    name: String,
    score: Number,
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.button {
  max-width: "50rem";
}
</style>
