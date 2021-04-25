<template>
  <div id="app" align-v="center" :style="{ backgroundColor: '#000036' }">
    <div id="nav">
      <router-link :to="'/home?group=' + $route.query.group"
        >Home Page</router-link
      >
      |
      <router-link :to="'/score?group=' + $route.query.group"
        >Scoreboard</router-link
      >
      |
      <router-link :to="'/about?group=' + $route.query.group"
        >About</router-link
      >
      <!-- |
      <router-link :to="'/secret/'">Secret</router-link> -->
    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
@import ".//assets/styles/custom.scss";
@import "../node_modules/bootstrap/scss/bootstrap.scss";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #ffffff;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
