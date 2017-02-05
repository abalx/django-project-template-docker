'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var autoprefixer = require('autoprefixer');
var rename = require('gulp-rename');
var cssmin = require('gulp-cssmin');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');
var webpackStream = require("webpack-stream");
var path = require('path');


var webpackConfig = require('./webpack.config.js');
var config = {
    buildPath: 'build/',

    css: {
        nameDev: 'bundle.css',
        nameProd: 'bundle.min.css',
        watchPath: 'apps/**/static/**/styles/**/*.scss',
        mainFilePath: 'assets/main.scss',
        includePaths: ['apps', 'vendor', 'node_modules'],
    },

    js: {
        nameDev: 'bundle.js',
        nameProd: 'bundle.min.js',
        mainFilePath: './assets/main.js',
        extensions: ['', '.js', 'jsx'],
        includePaths: [
            path.resolve('apps'),
            path.resolve('vendor'),
            path.resolve('node_modules'),
        ],
    }
}


gulp.task('sassDev', function(){
    var processors = [
        autoprefixer({browsers: ['>1%']}),
    ];

    return gulp.src(config.css.mainFilePath)
        .pipe(sourcemaps.init())
        .pipe(sass({includePaths: config.css.includePaths}).on('error', sass.logError))
        .pipe(postcss(processors))
        .pipe(rename(config.css.nameDev))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(config.buildPath))
});


gulp.task('sassProd', function(){
    var processors = [
        autoprefixer({browsers: ['>1%']}),
    ];

    return gulp.src(config.css.mainFilePath)
        .pipe(sass({includePaths: config.css.includePaths}))
        .pipe(postcss(processors))
        .pipe(cssmin())
        .pipe(rename(config.css.nameProd))
        .pipe(gulp.dest(config.buildPath))
});


gulp.task('jsDev', function () {
    return gulp.src(config.js.mainFilePath)
        .pipe(webpackStream(
            Object.assign({}, webpackConfig.dev, {
                entry: config.js.mainFilePath,
                output: {filename: config.js.nameDev},
                resolve: {
                    root: config.js.includePaths,
                    extensions: config.js.extensions,
                },
            }))
        )
        .on('error', function (error) {
            console.log(error.message);
            this.emit('end');
        })
        .pipe(gulp.dest(config.buildPath));
});


gulp.task('jsProd', function () {
    return gulp.src(config.js.mainFilePath)
        .pipe(webpackStream(
            Object.assign({}, webpackConfig.prod, {
                entry: config.js.mainFilePath,
                output: {filename: config.js.nameProd},
                resolve: {
                    root: config.js.includePaths,
                    extensions: config.js.extensions,
                },
            }))
        )
        .pipe(gulp.dest(config.buildPath));
});


gulp.task('watch', function() {
    gulp.watch([config.css.watchPath, config.css.mainFilePath], ['sassDev']);
});


gulp.task('default', ['watch', 'sassDev', 'jsDev',]);
gulp.task('production', ['sassProd', 'jsProd',]);