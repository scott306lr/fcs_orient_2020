<template>
  <div class="backend">
    <Clock />
    <b-input-group prepend="更改公告文字">
      <b-form-input v-model="input_cdtext" placeholder=""></b-form-input>
      <template #append>
        <b-button @click="cdtextUpdate(input_cdtext)">更新公告</b-button>
        <b-button variant="primary" @click="changeFreeze()">
          凍結記分板
        </b-button>
      </template>
    </b-input-group>

    <br />

    <div>
      <a> 選擇隊伍： </a>
      <b-form-select class="w-50" v-model="selected_group" :options="g_options">
        <template #first>
          <b-form-select-option
            class="justify-content-center"
            :value="null"
            disabled
          >
            -- Select team --
          </b-form-select-option>
        </template>
      </b-form-select>
    </div>

    <div>
      <a> 加分原因： </a>
      <b-form-select
        class="w-50"
        v-model="selected_type"
        :options="type_options"
      >
        <template #first>
          <b-form-select-option
            class="justify-content-center"
            :value="null"
            disabled
          >
            -- Select reason --
          </b-form-select-option>
        </template>
      </b-form-select>
    </div>

    <b-input-group prepend="題目id">
      <b-form-input v-model="input_hid" placeholder=""></b-form-input>
    </b-input-group>

    <b-input-group prepend="增加隊伍分數">
      <b-form-input v-model="input_score" placeholder=""></b-form-input>
      <template #append>
        <b-button
          :disabled="input_hid === ''"
          @click="
            addScore(selected_group, input_hid, selected_type, input_score)
          "
        >
          加分
        </b-button>
      </template>
    </b-input-group>

    <!-- <b-input-group prepend="更改隊伍名稱">
      <b-form-input v-model="input_name" placeholder=""></b-form-input>
      <template #append>
        <b-button @click="changeName(selected_group, input_name)"
          >更名</b-button
        >
      </template>
    </b-input-group> -->

    <b-button block v-b-toggle.a1 variant="info">
      維護用，平時請勿使用
    </b-button>

    <b-collapse id="a1" accordion="my-accordion" role="tabpanel">
      <b-button
        squared
        variant="primary"
        :disabled="selected_group === null"
        @click="fetchHints(selected_group)"
      >
        檢視排組
      </b-button>

      <b-form-select class="w-50" v-model="selected_hints" :options="h_options">
        <template #first>
          <b-form-select-option
            class="justify-content-center"
            :value="null"
            disabled
          >
            -- Select hint --
          </b-form-select-option>
        </template>
      </b-form-select>

      <div>
        <b-button
          squared
          :disabled="selected_hints === null"
          @click="changeDone(selected_group, selected_hints)"
        >
          更改Done
        </b-button>

        <b-button
          squared
          :disabled="selected_hints === null"
          @click="changeAvail(selected_group, selected_hints)"
        >
          更改Avail
        </b-button>
      </div>

      <b-button
        squared
        :disabled="selected_hints === null"
        @click="open_hints(this.groups[i].id, 2)"
      >
        開放題目
      </b-button>

      <br />

      <!-- <b-input-group prepend="增減一般題ID">
        <b-form-input v-model="input_nmid" placeholder=""></b-form-input>
        <template #append>
          <b-button
            :disabled="input_nmid === ''"
            @click="addNormal(input_nmid)"
          >
            增加
          </b-button>
          <b-button
            :disabled="input_nmid === ''"
            @click="deleteNormal(input_nmid)"
          >
            刪除
          </b-button>
        </template>
      </b-input-group> -->

      <b-input-group prepend="增減特殊題ID">
        <b-form-input v-model="input_spid" placeholder=""></b-form-input>
        <template #append>
          <b-button
            :disabled="input_spid === ''"
            @click="addSpecial(input_spid)"
          >
            增加
          </b-button>
          <b-button
            :disabled="input_spid === ''"
            @click="deleteSpecial(input_spid)"
          >
            刪除
          </b-button>
        </template>
      </b-input-group>

      <b-input-group prepend="增加隊伍">
        <b-form-input
          v-model="input_genid"
          placeholder="group id"
        ></b-form-input>
        <template #append>
          <b-button
            @click="addGroup(input_genid)"
            :disabled="input_genid === ''"
            >add group</b-button
          >
        </template>
      </b-input-group>

      <b-button squared variant="primary" v-b-modal="'logging'"> Log </b-button>

      <br />

      <b-button squared variant="primary" @click="deleteGroup(selected_group)">
        刪除該隊伍
      </b-button>

      <br />
      <br />

      <b-button squared variant="primary" @click="Initialize()">
        初始化
      </b-button>

      <b-modal
        id="logging"
        size="lg"
        title="Logging"
        hide-footer
        centered
        scrollable
      >
        <GroupLog gid="0" admin="yes" />
      </b-modal>

      <br />
    </b-collapse>
    <!-- 增加隊伍、隊伍改分數、換題目、題目解鎖、題目完成、改題目分數、bonus etc -->
  </div>
</template>

<script>
import Clock from "../components/Clock.vue";
import GroupLog from "../components/GroupLog.vue";

export default {
  name: "Secret",
  components: {
    Clock,
    GroupLog,
  },
  data() {
    return {
      freeze: String,
      hint: JSON,
      hints: JSON,
      group: JSON,
      groups: [],
      input_cdtext: "",
      input_name: "",
      input_score: "",
      input_hid: "",
      input_genid: "",
      input_nmid: "",
      input_spid: "",
      selected_group: 0,
      selected_hints: 0,
      selected_type: 0,
      g_options: [],
      h_options: [],
      type_options: [
        {
          text: "回答工人謎題",
          value: 0,
        },
        {
          text: "完成上傳照片",
          value: 1,
        },
        {
          text: "分數錯誤修正",
          value: 2,
        },
      ],
    };
  },
  mounted() {
    this.fetchGroups();
    this.fetchOthers();
    //this.fetchHints(this.groups[this.selected_group].id);
  },
  created() {
    //this.group_id = this.$route.query.group;
  },
  methods: {
    async logging(gid, reason, curScore, addScore) {
      var date = new Date();
      var hhmmss =
        date.getHours().toString().padStart(2, "0") +
        ":" +
        date.getMinutes().toString().padStart(2, "0") +
        ":" +
        date.getSeconds().toString().padStart(2, "0");

      await this.axios
        .post("/backend/logging/", {
          group_id: gid,
          reason: reason,
          fin_time: hhmmss,
          cur_score: curScore,
          get_score: addScore,
        })
        .then(function (response) {
          return response.data;
        });
    },
    async fetchOthers() {
      const val_s = await this.axios
        .get("/backend/others/1/")
        .then(function (response) {
          return response.data;
        });
      //this.input_cdtext = val_s.cd_text;
      this.freeze = val_s.freeze;
    },
    async fetchHints(gid) {
      const val_groupinfo = await this.axios
        .get("/backend/groupsinfo/" + this.groups[gid].id + "/")
        .then(function (response) {
          return response.data;
        });
      const val_hints = val_groupinfo.hints;

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

      if (name.length > 25) {
        alert("同學你隊伍名稱也設太長了吧");
        return;
      }

      const val_groups = await this.axios
        .get("/backend/groups/")
        .then(function (response) {
          return response.data;
        });
      this.groups = val_groups;

      if (confirm("確認更改隊名?")) {
        await this.axios
          .patch("/backend/groups/" + this.groups[gid].id + "/", {
            name: name,
          })
          .then(function (response) {
            return response.data;
          });
        alert("更名成功！");
      }
    },
    async cdtextUpdate(text) {
      if (confirm("new cdtext: " + text)) {
        await this.axios.patch("/backend/others/1/", {
          cd_text: text,
        });
      }
    },
    async addScore(gid, hid, selected, score) {
      if (score === "") {
        alert("分數欄不可為空！");
        return;
      }

      const val_groups = await this.axios
        .get("/backend/groups/")
        .then(function (response) {
          return response.data;
        });
      this.groups = val_groups;

      var newscore = this.groups[gid].score + parseInt(score);
      var text =
        "隊伍" +
        gid +
        ": " +
        this.groups[gid].name +
        "\n目前分數：" +
        this.groups[gid].score +
        "\n更改後分數：" +
        newscore;

      if (confirm(text)) {
        this.groups[gid].score = newscore;
        await this.axios
          .patch("/backend/groups/" + this.groups[gid].id + "/", {
            score: this.groups[gid].score,
          })
          .then(function (response) {
            return response.data;
          });

        switch (selected) {
          case 0:
            await this.logging(
              this.groups[gid].id,
              "回答謎題",
              this.groups[gid].score,
              score
            );
            break;
          case 1:
            await this.logging(
              this.groups[gid].id,
              "id:" + hid + " 審查完成",
              this.groups[gid].score,
              score
            );
            break;
          default:
            await this.logging(
              this.groups[gid].id,
              "修正分數錯誤",
              this.groups[gid].score,
              score
            );
            break;
        }

        alert("加分成功！");
      }
      this.fetchGroups();
    },
    async changeDone(gid, hid) {
      const val_groupinfo = await this.axios
        .get("/backend/groupsinfo/" + this.groups[gid].id.toString() + "/")
        .then(function (response) {
          return response.data;
        });
      this.hints = val_groupinfo.hints;

      var change = "";
      if (this.hints[hid].done === "yes") change = "no";
      else change = "yes";

      var text = "done  " + this.hints[hid].done + " -> " + change;
      if (confirm(text)) {
        this.hints[hid].done = change;

        await this.axios
          .patch("/backend/hints/" + this.hints[hid].id.toString() + "/", {
            done: this.hints[hid].done,
          })
          .then(function (response) {
            return response.data;
          });
      }
    },
    async changeAvail(gid, hid) {
      const val_groupinfo = await this.axios
        .get("/backend/groupsinfo/" + this.groups[gid].id.toString() + "/")
        .then(function (response) {
          return response.data;
        });
      this.hints = val_groupinfo.hints;

      var change = "";
      if (this.hints[hid].avail === "yes") change = "no";
      else change = "yes";

      var text = "avail  " + this.hints[hid].avail + " -> " + change;
      if (confirm(text)) {
        this.hints[hid].avail = change;

        await this.axios
          .patch("/backend/hints/" + this.hints[hid].id.toString() + "/", {
            avail: this.hints[hid].avail,
          })
          .then(function (response) {
            return response.data;
          });
      }
    },

    async changeFreeze() {
      const val_s = await this.axios
        .get("/backend/others/1/")
        .then(function (response) {
          return response.data;
        });
      this.input_cdtext = val_s.cd_text;
      this.freeze = val_s.freeze;

      var change = "";
      if (this.freeze === "yes") change = "no";
      else change = "yes";

      var text = "freeze  " + this.freeze + " -> " + change;
      if (confirm(text)) {
        this.freeze = change;

        await this.axios
          .patch("/backend/others/1/", {
            freeze: this.freeze,
          })
          .then(function (response) {
            return response.data;
          });
      }
    },

    async addGroup(genid) {
      if (confirm(`Add new group with id:${genid}?`)) {
        const val_groups = await this.axios
          .get("/backend/groups/")
          .then(function (response) {
            return response.data;
          });
        this.groups = val_groups;

        await this.axios
          .post("/backend/groupsinfo/", {
            id: genid,
            hints: [],
          })
          .then(function (response) {
            return response.data;
          });

        await this.axios
          .post("/backend/groups/", {
            id: genid,
            score: 0,
            name: "隊伍" + (parseInt(genid) % 1000),
          })
          .then(function (response) {
            return response.data;
          });
      }
    },

    async deleteGroup(gid) {
      if (confirm(`Delete group id:${this.groups[gid].id}?`)) {
        const val_groups = await this.axios
          .get("/backend/groups/")
          .then(function (response) {
            return response.data;
          });
        this.groups = val_groups;

        await this.axios
          .delete("/backend/groupsinfo/" + this.groups[gid].id + "/")
          .then(function (response) {
            return response.data;
          });

        await this.axios
          .delete("/backend/groups/" + this.groups[gid].id + "/")
          .then(function (response) {
            return response.data;
          });
      }
    },

    async deleteHintsLog() {
      const val_logging = await this.axios
        .get("/backend/logging/")
        .then(function (response) {
          return response.data;
        });

      for (var i = val_logging.length - 1; i >= 0; --i) {
        await this.axios
          .delete("/backend/logging/" + val_logging[i].id + "/")
          .then(function (response) {
            return response.data;
          });
      }

      const val_hints = await this.axios
        .get("/backend/hints/")
        .then(function (response) {
          return response.data;
        });

      for (i = val_hints.length - 1; i >= 0; --i) {
        await this.axios
          .delete("/backend/hints/" + val_hints[i].id + "/")
          .then(function (response) {
            return response.data;
          });
      }

      console.log("deleted all.");
    },

    async open_hints(gid, open_cnt) {
      const val_groupinfo = await this.axios
        .get("/backend/groupsinfo/" + gid + "/")
        .then(function (response) {
          return response.data;
        });
      this.hints = val_groupinfo.hints;

      var locked = [];
      for (var i = 0; i < this.hints.length; ++i) {
        if (this.hints[i].avail === "no") {
          locked.push(i);
        }
      }

      var cnt = Math.min(open_cnt, locked.length);
      while (cnt > 0) {
        var j = Math.floor(Math.random() * locked.length);
        var did = locked[j];
        console.log(did);
        this.hints[did].avail = "yes";
        locked.splice(j, 1);

        await this.axios
          .patch("/backend/hints/" + this.hints[did].id + "/", {
            avail: this.hints[did].avail,
          })
          .then(function (response) {
            return response.data;
          });
        cnt -= 1;
        console.log("unlocked hint " + this.hints[did].hint_id);
      }
      console.log(gid + " opened " + open_cnt + " hints.");
    },
    async addSpecial(hid) {
      if (hid <= 100) {
        alert("hid 小於 100！");
        return;
      }
      if (confirm("增加特殊題目 hint_id:" + hid)) {
        const val_groups = await this.axios
          .get("/backend/groups/")
          .then(function (response) {
            return response.data;
          });
        this.groups = val_groups;

        const val_hint = await this.axios
          .get("/backend/hint/" + hid + "/")
          .then(function (response) {
            return response.data;
          });

        var allgroups = [];
        for (var i = 0; i < this.groups.length; ++i) {
          allgroups.push(this.groups[i].id);
        }

        await this.axios
          .post("/backend/hints/", {
            hint_id: hid,
            done_by: 0,
            avail: "yes",
            done: "no",
            where: val_hint.where,
            whichgroup: allgroups,
          })
          .then(function (response) {
            return response.data;
          });
        console.log("added id:" + hid);
      }
    },

    async deleteSpecial(hid) {
      if (confirm("刪除特殊題目 hint_id:" + hid)) {
        const val_hints = await this.axios
          .get("/backend/hints/")
          .then(function (response) {
            return response.data;
          });

        var todelete;
        for (var i = 0; i < val_hints.length; ++i) {
          if (val_hints[i].hint_id === hid) {
            todelete = val_hints[i].id;
            break;
          }
        }

        await this.axios
          .delete("/backend/hints/" + todelete + "/")
          .then(function (response) {
            return response.data;
          });
        console.log("delete id:" + todelete);
      }
    },

    async addNormal(hid) {
      if (confirm("增加一般題目 hint_id:" + hid)) {
        const val_groups = await this.axios
          .get("/backend/groups/")
          .then(function (response) {
            return response.data;
          });
        this.groups = val_groups;

        const val_hint = await this.axios
          .get("/backend/hint/" + hid + "/")
          .then(function (response) {
            return response.data;
          });

        for (var i = 0; i < this.groups.length; ++i) {
          await this.axios
            .post("/backend/hints/", {
              hint_id: hid,
              done_by: 0,
              avail: "yes",
              done: "no",
              where: val_hint.where,
              whichgroup: [this.groups[i].id],
            })
            .then(function (response) {
              return response.data;
            });
        }

        console.log("added id:" + hid);
      }
    },

    async deleteNormal(hid) {
      if (confirm("刪除一般題目 hint_id:" + hid)) {
        const val_hints = await this.axios
          .get("/backend/hints/")
          .then(function (response) {
            return response.data;
          });

        var todelete;
        for (var i = 0; i < val_hints.length; ++i) {
          if (val_hints[i].hint_id === hid) {
            await this.axios
              .delete("/backend/hints/" + val_hints[i].id + "/")
              .then(function (response) {
                return response.data;
              });
          }
        }

        console.log("delete id:" + todelete);
      }
    },

    async create() {
      const val_groups = await this.axios
        .get("/backend/groups/")
        .then(function (response) {
          return response.data;
        });
      this.groups = val_groups;

      const val_hint = await this.axios
        .get("/backend/hint/")
        .then(function (response) {
          return response.data;
        });

      for (var i = 0; i < val_hint.length; ++i) {
        if (val_hint[i].id > 100) continue;
        for (var j = 0; j < this.groups.length; ++j) {
          await this.axios
            .post("/backend/hints/", {
              hint_id: val_hint[i].id,
              done_by: 0,
              avail: "no",
              done: "no",
              where: val_hint[i].where,
              whichgroup: [this.groups[j].id],
            })
            .then(function (response) {
              return response.data;
            });
        }
      }

      for (i = 0; i < this.groups.length; ++i) {
        await this.axios
          .patch("/backend/groups/" + this.groups[i].id + "/", {
            score: 0,
          })
          .then(function (response) {
            return response.data;
          });
      }
      console.log("score all set to 0");

      console.log("create finished.");
    },

    async Initialize() {
      if (confirm("Initialize?")) {
        await this.deleteHintsLog();
        await this.create();
        for (var i = 0; i < this.groups.length; ++i) {
          await this.open_hints(this.groups[i].id, 5);
        }
        console.log("Initialize complete.");
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
