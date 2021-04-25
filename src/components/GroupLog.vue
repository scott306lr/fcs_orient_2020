<template>
  <div>
    <li v-for="alog in logging" :key="alog.id">
      {{ alog.fin_time }} 組別:{{ alog.group_id }} {{ alog.reason }}，獲得{{
        alog.get_score
      }}分。{{ "當前分數為" + alog.cur_score + "分" }}
    </li>
  </div>
</template>

<script>
export default {
  name: "GroupLog",
  components: {},
  props: {
    gid: String,
    admin: String,
  },
  data() {
    return {
      // Note `isActive` is left out and will not appear in the rendered table
      logging: [],
    };
  },
  mounted() {
    this.fetchLog();
    this.timer = setInterval(this.fetchLog, 4000);
  },
  methods: {
    async fetchLog() {
      const val = await this.axios
        .get("/backend/logging/")
        .then(function (response) {
          return response.data;
        });

      if (this.admin === "no") {
        var group_id = parseInt(this.gid);
        this.logging = val.filter((alog) => alog.group_id === group_id);
        console.log(val);
      } else {
        this.logging = val;
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
