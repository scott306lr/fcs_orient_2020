<template>
  <div class="about">
    <h1>FCS 2021 Orienteering!</h1>
    <h2>This page will include introduction and rules.</h2>
    <h2>introduction</h2>
    <p>
      你們一開始回拿到數張提示卡，
      找到圖中所在地點，完成卡片上的任務，即可獲得該卡片的分數，並解鎖更多謎題。
    </p>
    <p>
      在遊戲進行的最後45分鐘，我們會鎖住各小隊的記分板，你們將看不到對手的分數。請努力在這段時間裡完成題目，讓對手大吃一驚吧！
    </p>
    <h2>Rules</h2>
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
