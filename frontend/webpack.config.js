'use strict'
const webpack = require('webpack')
const { VueLoaderPlugin } = require('vue-loader')
//const HtmlWebpackPlugin = require('html-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const path = require('path')

var BundleTracker = require('webpack-bundle-tracker')


function resolve (dir) {
  return path.join(__dirname, '.', dir) //Es decir no hace nada
}

module.exports = {
  mode: 'development',

output: {
    path: path.resolve(__dirname, './dist'),
    publicPath: 'http://0.0.0.0:8080/dist/',
    filename: 'build.js' //filename: 'build-[hash].js'
},


  entry: [
    './src/main.js'
  ],
  devServer: {
    hot: true,
    watchOptions: {
      poll: true
    }
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      },
      { //Es importante que este loader este despeus del vue-loader
        test: /\.js$/,
        use: 'babel-loader'
      }
    ]
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new VueLoaderPlugin(),
    new BundleTracker({filename: './webpack-stats.json'}), //Eso sera algo asi como los logs.

    new CopyWebpackPlugin([{
    from: resolve('static'),
    to: resolve('dist/static'),
    toType: 'dir'
  }])
  ]
}