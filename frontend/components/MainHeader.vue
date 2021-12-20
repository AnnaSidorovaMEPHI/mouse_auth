<template>
  <header>
    <div class="center">
      <nav>
        <nuxt-link to="/users">Users</nuxt-link>
        <nuxt-link to="/orders">Orders</nuxt-link>
        <nuxt-link to="/transactions">Transactions</nuxt-link>
        <nuxt-link to="/reviews">Reviews</nuxt-link>
        <!-- <nuxt-link to="/about">About</nuxt-link> -->
        <!-- <nuxt-link to="/signup">Sign up</nuxt-link>
        <nuxt-link to="/signin">Sign in</nuxt-link> -->
      </nav>
      <div class="header_contacts pr-5">
        <div class="m-auto text-2xl text-white">Carsharing service</div>
        <div class="flex justify-around m-auto text-sm">
          <div>User recognition via mouse tracking</div>
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
  background-color: #c4b5fd;
}
nav a {
  padding: 20px;
  color: #fff;
  font-size: 18px;
  text-decoration: none;
  line-height: 1em;
}
nav a:hover {
  color: rgb(0, 0, 0);
}
nav a.nuxt-link-exact-active {
  color: rgb(0, 0, 0);
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
  box-sizing: border-box;
}
</style>
