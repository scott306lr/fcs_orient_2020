<template>
  <div>
    <b-card
      bg-variant="dark"
      text-variant="white"
      style="max-width: 30rem"
      class="mb-1"
    >
      <b-card-img-lazy
        :src="'./Hint_Images/' + hint_id + '.jpg'"
        alt="Image"
        bottom
      ></b-card-img-lazy>

      <b-card-body>
        <b-card-title>{{ hint.name }}</b-card-title>
        <b-card-sub-title class="mb-2"
          >題目難易度：{{ hint.difficulty }}</b-card-sub-title
        >
        <b-card-sub-title class="mb-2"
          >題目分數：{{ hint.basic_score }}分</b-card-sub-title
        >

        <b-card-text v-html="hint.text"></b-card-text>

        <b-collapse id="collapse_upload" v-model="uploadmode" class="mt-2">
          <b-form-file accept="image/*" v-model="file"></b-form-file>
          <b-button @click="uploadImage()">確認</b-button>
        </b-collapse>

        <b-collapse id="collapse_input" v-model="inputmode" class="mt-2">
          <b-input-group>
            <b-form-input
              v-model="input_text"
              placeholder="請輸入答案"
            ></b-form-input>

            <template #append>
              <b-button @click="checkAnswer(input_text)">確認</b-button>
            </template>
          </b-input-group>
        </b-collapse>
      </b-card-body>
    </b-card>
  </div>
</template>

<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/8.4.1/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
    https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="https://www.gstatic.com/firebasejs/8.4.1/firebase-analytics.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.4.1/firebase-storage.js"></script>

<script>
import firebase from "firebase/app";
import "firebase/analytics";
import "firebase/auth";
import "firebase/firestore";
import "firebase/storage";

export default {
  props: {
    id: Number,
    hint_id: Number,
    status: String,
  },
  computed: {},
  mounted() {
    this.fetchHint();
    this.fetchHints();
    this.fetchGroup();
  },
  created() {
    this.group_id = this.$route.query.group;
    //this.fetchData();
  },
  data() {
    return {
      hint: JSON,
      hints: [],
      group: JSON,
      input_text: "",
      uploadmode: false,
      inputmode: false,
      file: null,
    };
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

    async fetchHint() {
      const val_hint = await this.axios
        .get("/backend/hint/" + this.hint_id + "/")
        .then(function (response) {
          return response.data;
        });
      //console.log(val_hint);
      if (val_hint.hint_choices === 3) {
        this.uploadmode = true;
      } else {
        this.inputmode = true;
      }
      this.hint = val_hint;
    },

    async fetchHints() {
      const val_hints = await this.axios
        .get("/backend/groupsinfo/" + this.group_id + "/")
        .then(function (response) {
          return response.data;
        });
      this.hints = val_hints.hints;
    },

    async fetchGroup() {
      const val_group = await this.axios
        .get("/backend/groups/" + this.group_id + "/")
        .then(function (response) {
          return response.data;
        });
      this.group = val_group;
    },

    async hint_set_done(hid) {
      await this.axios
        .patch("/backend/hints/" + hid + "/", {
          done: "yes",
          done_by: this.group_id,
        })
        .then(function (response) {
          return response.data;
        });
      console.log("id " + hid + " set done.");
    },

    async add_score(score) {
      const val_group = await this.axios
        .get("/backend/groups/" + this.group_id + "/")
        .then(function (response) {
          return response.data;
        });
      this.group = val_group;

      this.group.score += score;
      await this.axios
        .patch("/backend/groups/" + this.group_id.toString() + "/", {
          score: this.group.score,
        })
        .then(function (response) {
          return response.data;
        });
      console.log("add score.");
    },

    async open_hints(open_cnt) {
      var locked = [];
      for (var i = 0; i < this.hints.length; ++i) {
        if (this.hints[i].avail === "no") {
          locked.push(i);
        }
      }

      var cnt = Math.min(open_cnt, locked.length);
      while (cnt > 0) {
        var i = Math.floor(Math.random() * locked.length);
        var did = locked[i];
        this.hints[did].avail = "yes";
        locked.splice(i, 1);

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
    },

    async checkAnswer(ans) {
      if (ans === "") {
        alert("答案不可為空！");
        return;
      }

      const val_checkhint = await this.axios
        .get("/backend/hints/" + this.id + "/")
        .then(function (response) {
          return response.data;
        });

      if (val_checkhint.done === "yes") {
        alert("題目已完成！");
        return;
      }

      if (confirm("確認輸入 " + ans + " ?")) {
        const val_group = await this.axios
          .get("/backend/groups/" + this.group_id + "/")
          .then(function (response) {
            return response.data;
          });
        this.group = val_group;

        const val_hints = await this.axios
          .get("/backend/groupsinfo/" + this.group_id + "/")
          .then(function (response) {
            return response.data;
          });
        this.hints = val_hints.hints;

        if (ans === this.hint["answer"]) {
          this.hint_set_done(this.id);
          this.block = await this.add_score(this.hint.basic_score);
          this.open_hints(2);

          await this.logging(
            this.group_id,
            "id:" + this.hint_id + " 完成題目",
            this.group.score,
            this.hint.basic_score
          );

          this.fetchHints();
          this.fetchGroup();

          alert("輸入正確！");
          alert("解鎖2題新題目！");
        } else {
          this.block = await this.add_score(-50);
          await this.logging(
            this.group_id,
            "id:" + this.hint_id + " 回答錯誤",
            this.group.score,
            "-50"
          );

          this.fetchHints();
          this.fetchGroup();
          alert("輸入錯誤！ 扣50分！");
        }
      }
    },

    async uploadImage() {
      if (this.file == null) {
        alert("請上傳照片！");
        return;
      }

      if (this.file != null) {
        var firebaseConfig = {
          apiKey: "AIzaSyDFopyMEVt8O0MTX4Mpzd7YGBCHyJL2aZ4",
          authDomain: "fcsorient2021.firebaseapp.com",
          projectId: "fcsorient2021",
          storageBucket: "fcsorient2021.appspot.com",
          messagingSenderId: "815641252619",
          appId: "1:815641252619:web:d795676ec96f145774c80e",
          measurementId: "G-XK9K1NYGS3",
        };
        // Initialize Firebase
        if (!firebase.apps.length) firebase.initializeApp(firebaseConfig);

        firebase.analytics();
        var date = new Date();
        var hhmmss =
          date.getHours().toString().padStart(2, "0") +
          "-" +
          date.getMinutes().toString().padStart(2, "0") +
          "-" +
          date.getSeconds().toString().padStart(2, "0");
        var re = /(?:\.([^.]+))?$/;
        var ext = re.exec(this.file["name"])[1];
        var filename = `group${"" + this.group_id}_hint${
          "" + this.id.toString().padStart(2, "0")
        }_${hhmmss}.${ext}`;
        console.log(filename);

        var imageRef = firebase.storage().ref().child(filename);
        imageRef.put(this.file).then((snapshot) => {
          console.log("Image Uploaded!");
        });
        alert("上傳完成！ 請等待審查結果！");
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
