<template>
  <div>
    <b-input-group prepend="隊伍編號">
      <b-form-input
        v-model="input_gid"
        placeholder="請輸入隊伍編號"
      ></b-form-input>
      <template #append>
        <b-button
          variant="primary"
          :disabled="input_gid === ''"
          :to="'/home?group=' + input_gid"
        >
          confirm
        </b-button>
      </template>
    </b-input-group>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "Select",
  components: {},
  mounted() {},
  data() {
    return {
      input_gid: "",
    };
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
