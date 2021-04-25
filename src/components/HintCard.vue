<template>
  <div>
    <b-card
      :header="header"
      header-text-variant="dark"
      header-bg-variant="white"
      :bg-variant="where"
      text-variant="white"
      style="max-width: 30rem"
      class="mb-1"
    >
      <b-card-img-lazy
        :src="'./Hint_Images/' + hint_id + '.jpg'"
        :alt="'Image ' + hint_id"
        bottom
      ></b-card-img-lazy>

      <b-card-body>
        <b-card-title>{{ name }}</b-card-title>
        <b-card-sub-title class="mb-2">
          <strong> hint id: {{ hint_id }} </strong>
        </b-card-sub-title>

        <b-button
          pill
          :disabled="this.status === 'yes' ? true : false"
          v-b-modal="'modal' + id"
        >
          查看
        </b-button>
        <b-modal
          :id="'modal' + id"
          size="lg"
          title="詳細資訊"
          hide-footer
          centered
          scrollable
        >
          <HintDetails :id="id" :hint_id="hint_id" />
        </b-modal>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "HintCard",
  components: {
    HintDetails: () => import("./HintDetails"),
  },
  props: {
    id: Number,
    hint_id: Number,
    name: String,
    status: String,
    where: String,
    header: String,
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.yes {
  background: green;
}
.no {
  background: red;
}
</style>
