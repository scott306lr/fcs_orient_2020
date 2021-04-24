<template>
  <div class="score">
    <Clock />
    <ScoreBoard :myid="group_id" />
  </div>
</template>

<script>
import ScoreBoard from "../components/ScoreBoard.vue";
import Clock from "../components/Clock.vue";

export default {
  name: "Score",
  components: {
    ScoreBoard,
    Clock,
  },
  created() {
    this.group_id = this.$route.query.group;
  },
  methods: {},
};
</script>
