<template>
  <div>
    <li v-for="alog in logging" :key="alog.id">
      {{ alog.fin_time }} 組別:{{ alog.group_id }}

      <p>
        {{ alog.reason }} 得
        <span :style="{ color: alog.color, fontWeight: 'bold' }"
          >{{ alog.get_score }}
        </span>
        分
      </p>
      <p>
        目前得分 <strong> {{ alog.cur_score }} </strong>分
      </p>
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
      log_text: [],
      color: "blue",
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

      this.logging.forEach(
        (alog) => (alog.color = alog.get_score > 0 ? "green" : "red")
      );
      //this.logging.reverse();
    },
  },
};
</script>

<style lang="scss" scoped>
li {
  margin: 15px 0 -5px;
}

p {
  margin: 0 20px;
}
</style>
