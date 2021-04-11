<template>
  <div class="about">
    <h1>This is an about page</h1>
    <b-alert
      :show="dismissCountDown"
      dismissible
      variant="warning"
      @dismissed="dismissCountDown = 0"
      @dismiss-count-down="countDownChanged"
    >
      This alert will dismiss after {{ dismissCountDown }} seconds...
    </b-alert>
    <b-button @click="showAlert" variant="info" class="m-1">
      Show alert with count-down timer
    </b-button>
  </div>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      dismissSecs: 5,
      dismissCountDown: 0,
    };
  },
  methods: {
    async fetchData() {
      const res = await fetch("hints.json");
      const val = await res.json();
      console.log(val);

      for (var i = 0; i < val.length; ++i) {
        if (val[i].done === "no") this.undone_hints.push(val[i]);
        else this.done_hints.push(val[i]);
      }
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
  },
};
</script>
