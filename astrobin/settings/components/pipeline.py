PIPELINE = {
    'PIPELINE_ENABLED': not DEBUG,
    'PIPELINE_COLLECTOR_ENABLED': not DEBUG,
    'JAVASCRIPT': {
        'scripts': {
            'source_filenames': (
                'common/fancybox/jquery.fancybox.js',

                'astrobin_apps_images/js/astrobin_apps_images.js',
                'astrobin_apps_images/js/jquery.capty.js',

                'js/jquery.i18n.js',
                'js/plugins/localization/jquery.localisation.js',
                'js/jquery.uniform.js',
                'js/jquery-ui-1.10.3.custom.min.js',
                'js/jquery-ui-timepicker-addon.js',
                'js/jquery.validationEngine-en.js',
                'js/jquery.validationEngine.js',
                'js/jquery.autoSuggest.js',
                'js/jquery.blockUI.js',
                'js/jquery.tmpl.1.1.1.js',
                'js/ui.multiselect.js',
                'js/jquery.form.js',
                'js/jquery.tokeninput.js',
                'js/jquery.flot.js',
                'js/jquery.flot.pie.min.js',
                'js/jquery.cycle.all.js',
                'js/jquery.easing.1.3.js',
                'js/jquery.multiselect.js',
                'js/jquery.qtip.js',
                'js/jquery.stickytableheaders.js',
                'js/jquery.timeago.js',
                'js/respond.src.js',
                'js/dfp.gpt.logger.override.js',
                'js/bootstrap.js',
                'js/astrobin.js',
            ),
            'output_filename': 'js/astrobin_pipeline_v' + MEDIA_VERSION + '.js',
        }
    },
    'STYLESHEETS': {
        'screen': {
            'source_filenames': (
                'css/jquery-ui.css',
                'css/jquery-ui-astrobin/jquery-ui-1.8.17.custom.css',
                'css/ui.multiselect.css',
                'css/validationEngine.jquery.css',
                'css/token-input.css',
                'css/jquery.multiselect.css',
                'css/jquery.qtip.css',

                'wysibb/theme/default/wbbtheme.css',

                'astrobin_apps_images/css/jquery.capty.css',
                'astrobin_apps_donations/css/astrobin_apps_donations.css',
                'astrobin_apps_premium/css/astrobin_apps_premium.css',

                'css/reset.css',
                'css/bootstrap.css',
                'css/bootstrap-responsive.css',

                'common/fancybox/jquery.fancybox.css',

                'css/astrobin.css',
                'css/astrobin-mobile.css',
            ),
            'output_filename': 'css/astrobin_pipeline_screen_v' + MEDIA_VERSION + '.css',
            'extra_content':  {
                'media': 'screen, projection',
            },
        }
    },
    'CSS_COMPRESSOR': 'pipeline.compressors.cssmin.CssminCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.jsmin.SlimItCompressor'
}
