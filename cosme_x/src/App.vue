<template>
  <q-tabs class="full-width-tabs" align="justify">
    <q-route-tab class="text-green" to="/" label="抽奖" />
    <q-route-tab class="text-purple" to="/records" label="记录" />
    <q-route-tab class="text-grey" to="/settings" label="设置" />
  </q-tabs>
  <router-view />
</template>

<style scoped>
html,
body {
  height: 100%;
  margin: 0;
  padding: 0;
}

body,
h1,
p,
div {
  text-align: center;
}

body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.full-width-tabs .q-tab {
  flex: 1;
  text-align: center;
}

h5 {
  margin: 10 0px;
}
</style>
