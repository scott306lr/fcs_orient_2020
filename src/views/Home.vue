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
      <b-card no-body class="mb-1" :style="{ backgroundColor: '#000036' }">
        <b-card-header
          header-tag="header"
          class="p-1"
          role="tab"
          :style="{ backgroundColor: '#000036' }"
        >
          <b-button block v-b-toggle.accordion1 variant="info"
            >未完成卡片</b-button
          >
        </b-card-header>
        <b-collapse
          id="accordion1"
          visible
          accordion="my-accordion"
          role="tabpanel"
          :style="{ backgroundColor: '#000036' }"
        >
          <b-card-body>
            <b-card-group deck>
              <HintCard
                v-for="hint in undone_hints"
                :key="hint.id"
                :id="hint.id"
                :hint_id="hint.hint_id"
                :where="hint.where"
                :header="hint.where == 'dark' ? '限定任務 (限一隊完成)' : null"
                :name="hint.name"
                :status="hint.done"
              >
              </HintCard>
            </b-card-group>
          </b-card-body>
        </b-collapse>
      </b-card>

      <b-card no-body class="mb-1" :style="{ backgroundColor: '#000036' }">
        <b-card-header
          header-tag="header"
          class="p-1"
          role="tab"
          :style="{ backgroundColor: '#000036' }"
        >
          <b-button block v-b-toggle.accordion-2 variant="info"
            >已完成卡片</b-button
          >
        </b-card-header>
        <b-collapse
          id="accordion-2"
          accordion="my-accordion"
          role="tabpanel"
          :style="{ backgroundColor: '#000036' }"
        >
          <b-card-body>
            <b-card-group deck>
              <HintCard
                v-for="hint in done_hints"
                :key="hint.id"
                :id="hint.id"
                :hint_id="hint.hint_id"
                :where="hint.where"
                :header="'完成隊伍： ' + group_names[hint.done_by]"
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
      group_names: {},
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
      var info = await this.axios
        .get("/backend/groupsinfo/" + this.group_id + "/")
        .then(function (response) {
          return response.data.hints;
        });

      var undone_sp_hints = [];
      var done_sp_hints = [];
      var undone_nm_hints = [];
      var done_nm_hints = [];
      for (var i = 0; i < info.length; ++i) {
        if (info[i].avail === "no") continue;

        if (info[i].done === "no") {
          if (info[i].hint_id > 100) {
            info[i].where = "dark";
            undone_sp_hints.push(info[i]);
          } else undone_nm_hints.push(info[i]);
        } else {
          if (info[i].hint_id > 100) {
            info[i].where = "dark";
            done_sp_hints.push(info[i]);
          } else done_nm_hints.push(info[i]);
        }

        this.undone_hints = undone_sp_hints.concat(undone_nm_hints);
        this.done_hints = done_sp_hints.concat(done_nm_hints);
      }

      const val_groups = await this.axios
        .get("/backend/groups/")
        .then(function (response) {
          return response.data;
        });

      this.group_names = {};
      for (i = 0; i < val_groups.length; ++i) {
        this.group_names[val_groups[i].id] = val_groups[i].name;
      }
    },

    async changeName(name) {
      if (name === "") {
        alert("隊伍名稱不可為空！");
        return;
      }
      if (confirm("確認更改隊名?")) {
        await this.axios
          .patch("/backend/groups/" + this.group_id + "/", {
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
