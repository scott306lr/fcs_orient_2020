<template>
  <div>
    <b-table
      head-variant="dark"
      striped
      hover
      :items="groups"
      :fields="fields"
    ></b-table>
  </div>
</template>

<script>
export default {
  name: "ScoreBoard",
  components: {},
  props: {
    myid: String,
  },
  data() {
    return {
      // Note `isActive` is left out and will not appear in the rendered table
      fields: [
        {
          key: "name",
        },
        {
          key: "score",
          sortable: true,
        },
      ],

      groups: Array,
    };
  },
  mounted() {
    this.fetchData();
    this.timer = setInterval(this.fetchData, 5000);
  },
  methods: {
    async fetchData() {
      const val = await this.axios
        .get("/backend/groups/")
        .then(function (response) {
          return response.data;
        });

      for (var i = 0; i < val.length; ++i) {
        if ((i + 1).toString() === this.myid) {
          val[i]["_rowVariant"] = "secondary";
        }
      }
      //console.log(val);
      //console.log(this.myid);
      this.groups = val;
    },
  },
};
</script>

<style lang="scss" scoped>
.yes {
  background: green;
}
.no {
  background: red;
}
</style>
