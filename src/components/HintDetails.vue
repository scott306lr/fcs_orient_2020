<template>
  <div>
    <a> {{ group_id }} </a>
    <b-card
      bg-variant="dark"
      text-variant="white"
      style="max-width: 30rem"
      class="mb-1"
    >
      <b-card-img-lazy :src="id + '.jpg'" alt="Image" bottom></b-card-img-lazy>

      <b-card-body>
        <b-card-title>{{ hint.name }}</b-card-title>
        <b-card-sub-title class="mb-2">{{ hint.difficulty }}</b-card-sub-title>
        <b-card-text>{{ hint.text }}</b-card-text>

        <b-input-group>
          <b-form-input
            v-model="input_text"
            placeholder="請輸入答案"
          ></b-form-input>

          <template #append>
            <b-button @click="checkAnswer(input_text)">確認</b-button>
          </template>
        </b-input-group>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    status: String,
  },
  computed: {},
  mounted() {},
  created() {
    this.group_id = this.$route.query.group;
    this.fetchData();
  },
  data() {
    return {
      hint: JSON,
      hints: JSON,
      group: JSON,
      input_text: "",
    };
  },
  methods: {
    async fetchData() {
      const val_hint = await this.axios
        .get("/backend/hint/" + this.id + "/")
        .then(function (response) {
          return response.data;
        });
      this.hint = val_hint;
      const val_hints = await this.axios
        .get("/backend/groupsinfo/" + this.group_id + "/")
        .then(function (response) {
          return response.data;
        });
      this.hints = val_hints.hints;
      const val_group = await this.axios
        .get("/backend/groups/" + this.group_id + "/")
        .then(function (response) {
          return response.data;
        });
      this.group = val_group;
    },

    async hint_set_done(hint_id) {
      this.hints[hint_id].done = "yes";
      console.log(hint_id);
      console.log(this.hints[hint_id]);

      await this.axios
        .patch("/backend/groupsinfo/" + this.group_id + "/", {
          hints: this.hints,
        })
        .then(function (response) {
          return response.data;
        });
    },

    async add_score() {
      this.group["score"] += this.hint["score"];
      await this.axios
        .patch("/backend/groups/" + this.group_id.toString() + "/", {
          score: this.group.score,
        })
        .then(function (response) {
          return response.data;
        });
    },

    async open_hints() {
      var cnt = 0;
      for (var i = 0; i < this.hints.length; ++i) {
        cnt += this.hints[i].avail === "no";
      }
      Math.min(3, cnt);
      i = 0;
      while (cnt > 0) {
        i = (i + 1) % this.hints.length;

        if (this.hints[i].avail === "no" && Math.random() > 0.7) {
          this.hints[i].avail = "yes";
          await this.axios
            .patch("/backend/hints/" + this.group_id.toString() + "/", {
              hints: this.hints,
            })
            .then(function (response) {
              return response.data;
            });
          cnt -= 1;
        }
      }
    },

    async checkAnswer(ans) {
      if (ans === this.hint["answer"]) {
        // Show celebrations ??
        alert("輸入正確！");
        for (var i = 0; i < this.hints.length; ++i) {
          if (
            this.hints[i].id === this.hint.id &&
            this.hints[i].done === "no"
          ) {
            this.hint_set_done(i);
            console.log(i);
            //this.add_score();
            //console.log(i);
            //this.open_hints();
            //console.log(i);
            break;
          }
        }
      } else {
        alert("輸入錯誤！");
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
