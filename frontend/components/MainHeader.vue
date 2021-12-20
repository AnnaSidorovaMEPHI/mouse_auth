<template>
  <header>
    <div class="center">
      <nav>
        <nuxt-link to="/">Home</nuxt-link>
        <nuxt-link to="/cases">Storage</nuxt-link>
        <nuxt-link to="/signup">Sign up</nuxt-link>
        <nuxt-link to="/signin">Sign in</nuxt-link>
        <nuxt-link to="/info">Information</nuxt-link>
        <nuxt-link to="/about">About</nuxt-link>
      </nav>
      <div class="header_contacts">
        <div class="header_contacts--name">Zero Trust</div>
        <div class="header_contacts--info">
          <div>User recognition via mouse tracking</div>
          <!-- <a href="tel:79129125246">+7 912 912-52-46</a>
          <a href="mailto:email@emal.com" target="_blank">email@emal.com</a> -->
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {};
</script>

<style>
header {
  background-color: #9370DB;
}
nav a {
  padding: 20px;
  color: #fff;
  font-size: 18px;
  text-decoration: none;
  line-height: 1em;
}
nav a:hover {
  color: rgb(76, 126, 126);
}
nav a.nuxt-link-exact-active {
  color:#000080;
}
nav {
  display: flex;
}
.center {
  width: 1500px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
}
.header_contacts {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  font-weight: 500;
  line-height: 1em;
  padding: 4px 0px;
  box-sizing: border-box;
}
.header_contacts--name {
  color: #ffffff;
  margin: auto;
  font-size: 25px;
}
.header_contacts--info {
  margin: auto 0;
  font-size: 14px;
  display: flex;
  justify-content: space-around;
}
.header_contacts--info div {
  color: #000080;
}
</style>
