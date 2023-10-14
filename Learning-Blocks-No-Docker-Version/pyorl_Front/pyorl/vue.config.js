const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  configureWebpack: {
    plugins: [new MiniCssExtractPlugin()],
  },
  // Other configuration options go here
};
