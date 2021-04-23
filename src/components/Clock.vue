<template>
  <div>
    <countdown :end-time="new Date('Apr 30, 2021 21:00:00').getTime()">
      <template v-slot:process="cd">
        <h2>
          遊戲剩餘時間：{{
            `${cd.timeObj.ceil.h}:${cd.timeObj.m}:${cd.timeObj.s}`
          }}
        </h2>
      </template>
      <template v-slot:finish>
        <span>時間截止! 請盡速回到圖書館前集合！</span>
      </template>
    </countdown>
  </div>
</template>

<script>
export default {
  name: "Clock",
  components: {},
  props: {},
};
</script>

<style lang="scss" scoped></style>
