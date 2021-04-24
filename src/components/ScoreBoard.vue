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
      groups: [],
    };
  },
  mounted() {
    this.fetchData();
    this.timer = setInterval(this.fetchData, 5000);
  },
  methods: {
    async fetchData() {
      const val_s = await this.axios
        .get("/backend/others/1")
        .then(function (response) {
          return response.data;
        });
      //this.input_cdtext = val_s.cd_text;

      const val = await this.axios
        .get("/backend/groups/")
        .then(function (response) {
          return response.data;
        });

      for (var i = 0; i < val.length; ++i) {
        if (val[i].id.toString() === this.myid) {
          val[i]["_rowVariant"] = "secondary";
        }
      }

      if (val_s.freeze === "yes") {
        for (i = 0; i < val.length; ++i) {
          val[i]["score"] = "hidden";
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
