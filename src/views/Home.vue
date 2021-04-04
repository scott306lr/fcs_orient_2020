<template>
    <b-container>
        <h2>{{$route.query.group}}</h2>
        <b-card-group deck>
            <HintCard v-for="hint in undone_hints" :key="hint.id" :id="hint.id" :name="hint.name" :status="hint.done"> </HintCard>
        </b-card-group>
        <b-card-group deck>
            <HintCard v-for="hint in done_hints" :key="hint.id" :id="hint.id" :name="hint.name" :status="hint.done"> </HintCard>
        </b-card-group>
    </b-container>
</template>

<script>
import HintCard from '../components/HintCard.vue';
// @ is an alias to /src

export default {
    name: "Home",
    components: {
        HintCard
    },
    mounted() {
        this.group_id = this.$route.query.group
        this.fetchData();
    },
    data() {
        return {
            undone_hints: [],
            done_hints: [],
            group_id: Number,
        }
    },
    methods: {
        async fetchData() {
            const res = await fetch("hints.json");
            const val = await res.json();
            console.log(val);
            
            for (var i = 0; i < val.length; ++i) {
                if (val[i].done === "no")
                    this.undone_hints.push(val[i]);
                else
                    this.done_hints.push(val[i]);
            }
        },
    }
};
</script>
