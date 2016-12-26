var webpack = require("webpack");
var path = require('path');


var common = {
    context: __dirname,
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: [/node_modules/, '/vendor/'],
                loader: "babel-loader",
                query: {
                    presets: ['es2015', 'react', 'stage-0'],
                    comments: false
                }
            }
        ]
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery"
        }),
    ]
};


module.exports.dev = Object.assign({}, common, {
    watch: true,
    devtool: '#cheap-module-eval-source-map'
});


module.exports.prod = Object.assign({}, common, {
    plugins: common.plugins.concat([
        new webpack.optimize.UglifyJsPlugin({
            compress: {warnings: false},
            comments: false,
        })
    ])
});