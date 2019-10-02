module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
      pkg: grunt.file.readJSON('package.json'),

    less: {
      dev: {
        options: {
          path: ["static/less"],
          yuicompress: true,
          optimization: 2
        },
        files: {
          "static/css/main.css":["static/less/main.less","bower_components/lightbox/dist/css/lightbox.css"]
        }
      }
    },

    autoprefixer: {
      dev: {
        src: 'static/css/main.css'
      },
    },

    concat: {
      dev: {
        files: {
          'static/js/main.js': [
            'bower_components/jquery/dist/jquery.min.js',
            'bower_components/bootstrap/dist/js/bootstrap.min.js',
            'bower_components/jquery-cycle2/build/jquery.cycle2.min.js',
            'bower_components/lightbox/js/lightbox.js',
            'static/js/jquery.cycle2.swipe.min.js',
            'static/js/global.js',
          ]
        }
      }
    },

    uglify: {
      build: {
        files: {
          'static/js/main.min.js': ['static/js/main.js']
        }
      }
    },

    watch: {
      options: {
        livereload: true,
        nospawn: true
      },
      gruntfile: {
        files: ['Gruntfile.js']
      },
      js: {
        files: ['static/js/*.js'],
        tasks: ['concat:dev','uglify']
      },
      styles: {
        files: ['static/less/*.less'],
        tasks: ['less:dev','autoprefixer:dev']
      },
      markup: {
        files: ['*/*.py','*/*.html']
      }
    }

    });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-autoprefixer');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['watch']);
  grunt.registerTask('saveJS', ['concat','uglify']);

};