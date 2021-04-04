<template>
    <div>
        <b-card 
            bg-variant="dark"
            text-variant="white"
            style="max-width: 30rem"
            class="mb-1"
        > 

            <b-card-img-lazy :src="'https://picsum.photos/768/1080/?image='+id" alt="Image" bottom></b-card-img-lazy>

            <b-card-body>
                <b-card-title>{{hint.name}}</b-card-title>
                <b-card-sub-title class="mb-2">{{hint.difficulty}}</b-card-sub-title>
                <b-card-text>{{hint.text}}</b-card-text>
                
                <b-input-group>
                    <b-form-input :state="check" v-model="input_text" placeholder="請輸入答案"></b-form-input>

                    <template #append>
                        <b-button v-b-modal="'modal' + id" :to="'/home?group='+id"> 確認 </b-button>
                    </template>
                </b-input-group>
            </b-card-body>

        </b-card>
        <div>{{text}}</div>
    </div>
</template>

<script>
    export default {
        props: {
            id: Number,
            status: String
        },
        computed: {
            check() {
                return this.input_text === this.hint.answer ? true : false;
            },
        },
        mounted() {
            this.fetchData();
        },
        data() {
            return {
                hint: JSON,
                input_text: '',   
            }
        },
        methods: {
            async fetchData() {
                const res = await fetch("hint.json");
                const val = await res.json();
                this.hint = val;
                console.log(val)
            }
        }
    }
    
</script>

<style lang="scss" scoped>

</style>