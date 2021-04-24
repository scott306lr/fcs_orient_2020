<template>
  <b-container>
    <Clock />

    <div>
      <b-row class="justify-content-md-center">
        <b-col md="auto">
          <b-input-group prepend="隊伍名稱">
            <b-form-input
              v-model="input_text"
              :placeholder="group.name"
            ></b-form-input>
            <template #append>
              <b-button @click="changeName(input_text)">更名</b-button>
            </template>
          </b-input-group>
        </b-col>
      </b-row>

      <div>
        <b-button pill v-b-modal="'log' + group_id"> 查看得分紀錄 </b-button>
        <a> 分數：{{ this.group.score }} </a>
      </div>

      <b-modal
        :id="'log' + group_id"
        size="lg"
        title="得分紀錄"
        hide-footer
        centered
        scrollable
      >
        <GroupLog :gid="group_id" admin="no" />
      </b-modal>
    </div>

    <div class="accordion" role="tablist">
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion1 variant="info"
            >未完成卡片</b-button
          >
        </b-card-header>
        <b-collapse
          id="accordion1"
          visible
          accordion="my-accordion"
          role="tabpanel"
        >
          <b-card-body>
            <b-card-group deck>
              <HintCard
                v-for="hint in undone_hints"
                :key="hint.id"
                :id="hint.id"
                :name="hint.name"
                :status="hint.done"
                :where="hint.where"
              >
              </HintCard>
            </b-card-group>
          </b-card-body>
        </b-collapse>
      </b-card>

      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-2 variant="info"
            >已完成卡片</b-button
          >
        </b-card-header>
        <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-card-group deck>
              <HintCard
                v-for="hint in done_hints"
                :key="hint.id"
                :id="hint.id"
                :name="hint.name"
                :status="hint.done"
              >
              </HintCard>
            </b-card-group>
          </b-card-body>
        </b-collapse>
      </b-card>
    </div>
  </b-container>
</template>

<script>
import HintCard from "../components/HintCard.vue";
import Clock from "../components/Clock.vue";
import GroupLog from "../components/GroupLog.vue";
// @ is an alias to /src

export default {
  name: "Home",
  components: {
    HintCard,
    Clock,
    GroupLog,
  },
  mounted() {
    this.fetchData();
    this.timer = setInterval(this.fetchData, 4000);
  },
  created() {
    this.group_id = this.$route.query.group;
  },
  data() {
    return {
      undone_hints: [],
      done_hints: [],
      group: JSON,
      input_text: "",
    };
  },
  methods: {
    async fetchData() {
      const val = await this.axios
        .get("/backend/groups/" + this.group_id + "/")
        .then(function (response) {
          return response.data;
        });
      this.group = val;
      const info = await this.axios
        .get("/backend/groupsinfo/" + this.group_id + "/")
        .then(function (response) {
          return response.data.hints;
        });

      this.undone_hints = [];
      this.done_hints = [];
      for (var i = 0; i < info.length; ++i) {
        if (info[i].avail === "no") continue;
        if (info[i].done === "no") this.undone_hints.push(info[i]);
        else this.done_hints.push(info[i]);
      }
    },

    async changeName(name) {
      if (name === "") {
        alert("隊伍名稱不可為空！");
        return;
      }
      if (confirm("確認更改隊名?")) {
        await this.axios
          .patch("/backend/groups/" + this.group_id.toString() + "/", {
            name: name,
          })
          .then(function (response) {
            return response.data;
          });
        alert("更名成功！");
      }
    },
  },
};
</script>
