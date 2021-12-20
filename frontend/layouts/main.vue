<template>
  <div>
    <main-header />
    <Nuxt />
  </div>
</template>

<script>
import MainHeader from "~/components/MainHeader.vue";
export default {
  head() {
    return {
      link: [
        { rel: "canonical", href: `http://localhost:3000${this.$route.path}` }
      ]
    };
  },
  components: {
    MainHeader
  }
};
</script>

<style>
@font-face {
  font-family: Roboto-Bold;
  src: url("/fonts/Roboto-Bold.ttf");
}

@font-face {
  font-family: Roboto-Regular;
  src: url("/fonts/Roboto-Regular.ttf");
}
html,
body {
  font-family: Roboto-Regular, Roboto-Bold;
  font-size: 15px;
  margin: 0 auto;
  padding: 0;
  line-height: 1em;
}
</style>
