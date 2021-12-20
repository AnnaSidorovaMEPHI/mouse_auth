<template>
  <div>
    <main-header />
    <div class="center">
      <Nuxt />
    </div>
  </div>
</template>

<script>
import MainHeader from "~/components/MainHeader.vue";
export default {
  head() {
    return {
      link: [
        { rel: "canonical", href: `http://localhost:8000${this.$route.path}` },
      ],
    };
  },
  components: {
    MainHeader,
  },
};
</script>

<style>
html,
body {
  font-size: 15px;
  margin: 0 auto;
  padding: 0;
  line-height: 1em;
}
</style>
