var gulp = require('gulp'),
    sourcemaps = require('gulp-sourcemaps'),
    concat = require('gulp-concat'),
    babel = require('gulp-babel'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer');

var paths = {
    libs: [
    ],
    scripts: [
        'js/utils.js',
        'js/objects.js',
        'js/main.js'
    ],
    styles: [
        'css/main.scss'
    ]
};

gulp.task('default', ['compile-styles', 'compile-scripts', 'compile-libs']);

gulp.task('compile-styles', function() {
    return gulp.src(paths.styles)
        .pipe(sourcemaps.init())
            .pipe(sass({ outputStyle: 'compressed' }).on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('css'));
});

gulp.task('compile-scripts', function() {
    return gulp.src(paths.scripts)
        .pipe(sourcemaps.init())
            .pipe(babel({ presets: ['es2015'] }))
            .pipe(uglify().on('error', function(err){throw err;}))
            .pipe(concat('js/main.min.js'))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./'));
});

gulp.task('compile-libs', function() {
    return gulp.src(paths.libs)
        .pipe(sourcemaps.init())
            .pipe(babel({ presets: ['es2015'] }))
            .pipe(uglify().on('error', function(err){throw err;}))
            .pipe(concat('js/libs.min.js'))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./'));
});

gulp.task('build', function() {
    // do build stuff
});
