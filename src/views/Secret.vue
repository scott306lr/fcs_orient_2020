<template>
  <div class="backend">
    <b-button block v-b-toggle.a1 variant="info"
      >隊伍相關
    </b-button
    >
    <b-collapse
          id="a1"
          visible
          accordion="my-accordion"
          role="tabpanel"
        >

      <div>
        <a> Team <strong>{{  }}</strong> Selected </a>
        <b-form-select class="w-50" v-model="selected_group" :options="g_options">
          <template #first>
            <b-form-select-option
              class="justify-content-center"
              :value="null"
            >
              -- Select your team --
            </b-form-select-option>
          </template>
        </b-form-select>

        <b-button
          squared
          variant="primary"
          :disabled="selected_group === null"
          @click="fetchHints(groups[selected_group].id)"
        >
          檢視排組
        </b-button>
      </div>

      <b-input-group prepend="隊伍更改名稱">
        <b-form-input
          v-model="input_name"
          placeholder=""
        ></b-form-input>
        <template #append>
          <b-button @click="changeName(selected_group, input_name)">更名</b-button>
        </template>
      </b-input-group>

      <b-input-group prepend="隊伍增加分數">
        <b-form-input
          v-model="input_score"
          placeholder=""
        ></b-form-input>
        <template #append>
          <b-button @click="addScore(selected_group, input_score)">加分</b-button>
        </template>
      </b-input-group>

      <div>
        <a> <strong>{{ selected_hints }}</strong> Selected </a>

        <b-form-select class="w-50" v-model="selected_hints" :options="h_options">
          <template #first>
            <b-form-select-option
              class="justify-content-center"
              :value="null"
            >
              -- Select hint --
            </b-form-select-option>
          </template>
        </b-form-select>

        
      </div>

      
      <a> Done: "<strong>{{  }}</strong>" </a>

      <b-button
        squared
        variant="primary"
        :disabled="selected_group === null"
        @click="changeDone(hints[selected_hints].id)"
      >
        更改是否完成
      </b-button>

      <a> Avail: "<strong>{{ }}</strong>" </a>

      <b-button
        squared
        variant="primary"
        :disabled="selected_group === null"
        @click="changeAvail(hints[selected_hints].id)"
      >
        更改是否開啟
      </b-button>
    </b-collapse>
    <!-- 增加隊伍、隊伍改分數、換題目、題目解鎖、題目完成、改題目分數、bonus etc -->
  </div>
</template>

<script>
export default {
  name: "Secret",
  components: {},
  data() {
    return {
      hint: JSON,
      hints: JSON,
      group: JSON,
      groups: [],
      input_name: "",
      input_score: "",
      selected_group: 0,
      selected_hints: 0,
      g_options: [],
      h_options: [],
    };
  },
  mounted() {
    this.fetchGroups();
    //this.fetchHints(this.groups[this.selected_group].id);
  },
  created() {
    //this.group_id = this.$route.query.group;
  },
  methods: {
    // async fetchHint() {
    //   const val_hint = await this.axios
    //     .get("/backend/hint/" + this.id + "/")
    //     .then(function (response) {
    //       return response.data;
    //     });
    //   this.hint = val_hint;
    // },
    //this.hints[selected_hints].done 
    async fetchHints(gid) {
      console.log(gid);
      const val_groupinfo = await this.axios
        .get("/backend/groupsinfo/" + gid + "/")
        .then(function (response) {
          return response.data;
        });
      const val_hints = val_groupinfo.hints;
      console.log(val_hints);

      this.h_options = [];
      for (var i = 0; i < val_hints.length; i++) {
        var jsonData = {};
        jsonData["value"] = i; //val_hints[i]["id"];
        jsonData["text"] = "hint id: " + val_hints[i]["hint_id"];
        this.h_options.push(jsonData);
      }
      this.hints = val_hints;
    },
    async fetchGroups() {
      const val_groups = await this.axios
        .get("/backend/groups/")
        .then(function (response) {
          return response.data;
        });
      //this.groups = val_groups;
      this.g_options = [];
      for (var i = 0; i < val_groups.length; i++) {
        var jsonData = {};
        jsonData["value"] = i; //val_groups[i]["id"];
        jsonData["text"] = val_groups[i]["name"];
        this.g_options.push(jsonData);
      }
      this.groups = val_groups;
      console.log(this.groups);
      console.log(this.groups[this.selected_group].id);
    },

    async fetchGroup() {
      const val_group = await this.axios
        .get("/backend/groups/" + this.selected_group + "/")
        .then(function (response) {
          return response.data;
        });
      this.group = val_group;
    },

    async changeName(gid, name) {
      if (name === "") {
        alert("隊伍名稱不可為空！");
        return;
      }
      if (confirm("確認更改隊名?")) {
        await this.axios
          .patch("/backend/groups/" + gid.toString() + "/", {
            name: name,
          })
          .then(function (response) {
            return response.data;
          });
        alert("更名成功！");
      }
    },
    async addScore(gid, score) {
      if (score === "") {
        alert("分數欄不可為空！");
        return;
      }

      this.fetchGroups();

      var newscore = this.groups[gid].score + parseInt(score);
      var text = "隊伍" + gid + ": " + this.groups[gid].name + "\n目前分數：" + this.groups[gid].score + "\n更改後分數：" + newscore;

      if (confirm(text)) {
        await this.axios
          .patch("/backend/groups/" + this.groups[gid].id.toString() + "/", {
            score: newscore,
          })
          .then(function (response) {
            return response.data;
          });
        alert("加分成功！");
      }
    },
    async changeDone(hid) {
      var change = "";
      if (this.hints[hid].done === "yes") 
        change = "no";
      else 
        change = "yes";

      var text = "turn done from " + this.hints[hid].done + " to " + change;
      if (confirm(text)) {
        this.hints[hid].done = change;

        await this.axios
        .patch("/backend/hints/" + hid.toString() + "/", {
            avail: this.hints[hid].done,
          })
          .then(function (response) {
            return response.data;
          });
      }
    },
    async changeAvail(hid) {
      var change = "";
      if (this.hints[hid].avail === "yes") 
        change = "no";
      else 
        change = "yes";

      var text = "turn avail from " + this.hints[hid].avail + " to " + change;
      if (confirm(text)) {
        this.hints[hid].avail = change;

        await this.axios
        .patch("/backend/hints/" + hid.toString() + "/", {
            avail: this.hints[hid].avail,
          })
          .then(function (response) {
            return response.data;
          });
      }
    },
  },
};
</script>



<style lang="scss" scoped>
// .samecol {
//   display: flex;
//   justify-content: space-between;
// }
</style>