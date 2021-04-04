<template>
    <div>
        <b-card 
            bg-variant="dark"
            text-variant="white"
            style="max-width: 30rem"
            class="mb-1"
            :footer="status"
            :footer-class="status"
        > 

            <b-card-img-lazy :src="'https://picsum.photos/768/1080/?image='+id" alt="Image" bottom></b-card-img-lazy>

            <b-card-body>
                <b-card-title>{{name}}</b-card-title>
                <b-card-sub-title class="mb-2">id: {{id}}</b-card-sub-title>

                <b-button pill v-b-modal="'modal' + id" :to="'/home?group='+id"> 查看 </b-button>
                <b-modal :id="'modal' + id" size="lg" title="詳細資訊" hide-footer="true" centered scrollable>
                        <HintDetails :id="id" />
                </b-modal>
            </b-card-body>

        </b-card>
    </div>
</template>

<script>
    export default {
        name: "HintCard",
        components: {
            HintDetails: () => import("./HintDetails")
        },
        props: {
            id: Number,
            name: String,
            status: String
        },
        methods: {
        }
    }
</script>

<style lang="scss" scoped>

.yes{
    background: green;
}
.no{
    background: red;
}

</style>