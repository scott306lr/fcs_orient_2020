<template>
  <div>
    <countdown :end-time="new Date('Apr 30, 2021 21:00:00').getTime()">
      <template v-slot:process="cd">
        <h4>
          <strong>公告： {{ cd_text }}</strong>
        </h4>
        <h3>
          遊戲剩餘時間：{{
            `${cd.timeObj.ceil.h}:${cd.timeObj.m}:${cd.timeObj.s}`
          }}
        </h3>
      </template>
      <template v-slot:finish>
        <span>時間截止! 請盡速回到圖書館前集合！</span>
      </template>
    </countdown>
  </div>
</template>

<script>
export default {
  name: "Clock",
  components: {},
  props: {},
  data() {
    return {
      cd_text: "",
    };
  },
  mounted() {
    this.fetchData();
    this.timer = setInterval(this.fetchData, 5000);
  },
  methods: {
    async fetchData() {
      const val_s = await this.axios
        .get("/backend/others/1/")
        .then(function (response) {
          return response.data;
        });
      this.cd_text = val_s.cd_text;
    },
  },
};
</script>

<style lang="scss" scoped></style>
