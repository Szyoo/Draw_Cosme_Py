const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    target: 'electron-renderer',  // 添加这一行
    resolve: {
      fallback: {
        path: require.resolve("path-browserify"),
        fs: false  // 添加这一行
      }
    }
  },
});
