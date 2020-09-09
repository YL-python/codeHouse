<template>
  <div id="app">
    <ul>
      <li>
        <router-link to="/">home</router-link>
      </li>
      <li>
        <router-link to="/order">order</router-link>
      </li>
    </ul>
    <router-view />
  </div>
</template>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}
.left {
  float: left;
  width: 40%;
}
.right {
  float: left;
  width: 60%;
}
</style>
