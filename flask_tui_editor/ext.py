from flask import Blueprint, url_for
from markupsafe import Markup


class TUIEditor:
    """ Toast UI Editor class

        Usage Model

    ..  code-block:: python

       app = Flask(__name__)
       flask_tui_editor = TUIEditor(app=app, translations=["tr"], plugins=["uml", "chart"])

    or

    ..  code-block:: python

        flask_tui_editor = TUIEditor()

        def create_app():
            app = Flask(__name__)
            flask_tui_editor.init_app(app, translations=["tr"], plugins=["uml", "chart"])
            return app

    """

    def __init__(self, app, translations=(), plugins=()):
        self.translations = translations
        self.plugins = plugins
        self.static_url_path = None

        self.init_app(app=app, translations=translations, plugins=plugins)

    def context_processor(self):
        return dict(flask_tui_editor=self)

    def init_app(self, app: object, translations: list = (), plugins: list = ()) -> object:
        """

        :param app: Flask application
        :param translations: List of I18N language codes supported by Toast UI editor. See: https://github.com/nhn/tui.editor/blob/master/docs/en/i18n.md
        :param plugins: List of plugin names supported by Toast UI editor. See: https://github.com/nhn/tui.editor/blob/master/docs/en/plugin.md
        """
        app.context_processor(self.context_processor)
        self.translations = translations
        self.plugins = plugins
        self.static_url_path = app.static_url_path + '/flask_tui_editor'
        tui_editor_bp = Blueprint('flask_tui_editor', __name__, static_folder='static',
                                  static_url_path=self.static_url_path)
        app.register_blueprint(tui_editor_bp)

    @property
    def js(self):
        """ Loads the Toast UI Editor Javascript files.

        Plugins and translations are not loaded by default.
        Define them in the :obj:`TUIEditor <flask_tui_editor.ext.TUIEditor>` class in order to use them.

        Accessible as ``{{flask_tui_editor.js}}`` in Jinja2.
        """
        essential_files = [
            'js/toastui-editor-all.min.js',
            'js/toastui-editor-init.js'
        ]

        translations_files = {
            "ar": 'js/i18n/ar.js',
            "zh-CN": 'js/i18n/zh-cn.js',
            "zh-TW": 'js/i18n/zh-tw.js',
            "hr": 'js/i18n/hr-hr.js',
            "hr-HR": 'js/i18n/hr-hr.js',
            "cs": 'js/i18n/cs-cz.js',
            "cs-CZ": 'js/i18n/cs-cz.js',
            "nl": 'js/i18n/nl-nl.js',
            "nl-NL": 'js/i18n/nl-nl.js',
            "en": 'js/i18n/en-us.js',
            "en-US": 'js/i18n/en-us.js',
            "fi": 'js/i18n/fi-fi.js',
            "fi-FI": 'js/i18n/fi-fi.js',
            "fr": 'js/i18n/fr-fr.js',
            "fr-FR": 'js/i18n/fr-fr.js',
            "gl": 'js/i18n/gl-es.js',
            "gl-ES": 'js/i18n/gl-es.js',
            "de": 'js/i18n/de-de.js',
            "de-DE": 'js/i18n/de-de.js',
            "it": 'js/i18n/it-it.js',
            "it-IT": 'js/i18n/it-it.js',
            "ja": 'js/i18n/ja-jp.js',
            "ja-JP": 'js/i18n/ja-jp.js',
            "ko": 'js/i18n/ko-kr.js',
            "ko-KR": 'js/i18n/ko-kr.js',
            "nb": 'js/i18n/nb-no.js',
            "nb-NO": 'js/i18n/nb-no.js',
            "pl": 'js/i18n/pl-pl.js',
            "pl-PL": 'js/i18n/pl-pl.js',
            "pt": 'js/i18n/pt-br.js',
            "pt-BR": 'js/i18n/pt-br.js',
            "ru": 'js/i18n/ru-ru.js',
            "ru-RU": 'js/i18n/ru-ru.js',
            "es": 'js/i18n/es-es.js',
            "es-ES": 'js/i18n/es-es.js',
            "sv": 'js/i18n/sv-se.js',
            "sv-SE": 'js/i18n/sv-se.js',
            "tr": 'js/i18n/tr-tr.js',
            "tr-TR": 'js/i18n/tr-tr.js',
            "uk": 'js/i18n/uk-ua.js',
            "uk-UA": 'js/i18n/uk-ua.js'
        }

        plugin_files = {
            "chart": "js/plugins/chart.min.js",
            "code-syntax-highlight": "js/plugins/code-syntax-highlight.min.js",
            "color-syntax": "js/plugins/color-syntax.min.js",
            "table-merged-cell": "js/plugins/table-merged-cell.min.js",
            "uml": "js/plugins/uml.min.js",
        }

        selected_translation_files = [translations_files[translation] for translation in self.translations]
        selected_plugin_files = [plugin_files[plugin] for plugin in self.plugins]

        selected_files = [*essential_files, *selected_translation_files, *selected_plugin_files]

        return Markup("\n".join(
            [f"""<script src="{url_for('flask_tui_editor.static', filename=path)}"></script>""" for path in
             selected_files]))

    @property
    def css(self):
        """ Loads the Toast UI Editor Javascript files.

        Accessible as ``{{flask_tui_editor.js}}`` in Jinja2.
        """
        files = [
            'css/toastui-editor.min.css',
            'css/toastui-editor-dark.min.css',
        ]

        return Markup("\n".join(
            [f"""<link rel="stylesheet" href="{url_for('flask_tui_editor.static', filename=path)}">""" for path in
             files]))
