<template>
  <div>
    <li v-for="alog in logging" :key="alog.id">
      {{ alog.fin_time }} 完成題目 id:{{
        alog.fin_hint_id.toString().padStart(3, "0")
      }}，獲得{{ alog.get_score }}分。{{ "當前分數為" + alog.cur_score + "分" }}
    </li>
  </div>
</template>

<script>
export default {
  name: "GroupLog",
  components: {},
  props: {
    gid: String,
  },
  data() {
    return {
      // Note `isActive` is left out and will not appear in the rendered table
      logging: [],
    };
  },
  mounted() {
    this.fetchLog(this.gid);
  },
  methods: {
    async fetchLog(gid) {
      const val = await this.axios
        .get("/backend/logging/")
        .then(function (response) {
          return response.data;
        });
      var group_id = parseInt(gid);
      this.logging = val.filter((alog) => alog.group_id === group_id);
      console.log(val);
    },
  },
};
</script>

<style lang="scss" scoped></style>
