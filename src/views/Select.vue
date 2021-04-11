<template>
  <div>
    <b-form-select class="w-50" v-model="selected" :options="options">
      <template #first>
        <b-form-select-option
          class="justify-content-center"
          :value="null"
          disabled
          >-- Select your team --</b-form-select-option
        >
      </template>
    </b-form-select>
    <div class="mt-3">
      Selected: <strong>{{ selected }}</strong>
    </div>
    <b-button squared variant="primary" :to="'/home?group=' + selected">
      confirm
    </b-button>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "Select",
  components: {},
  mounted() {
    this.fetchData();
  },
  data() {
    return {
      selected: null,
      options: [],
      groups: [],
    };
  },
  methods: {
    async fetchData() {
      const res = await fetch("groups.json");
      const val = await res.json();
      console.log(val);

      for (var i = 0; i < val.length; i++) {
        var jsonData = {};
        jsonData["value"] = val[i]["id"];
        jsonData["text"] = val[i]["name"];
        this.options.push(jsonData);
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
