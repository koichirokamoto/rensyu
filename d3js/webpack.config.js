const path = require('path');

module.exports = {
  entry: './src/index.ts',
  output: {
    filename: 'index.js',
    path: path.resolve('dist'),
  },
  module: {
    rules: [{ test: /\.ts$/, use: 'ts-loader' }],
  },
  mode: 'development',
};
