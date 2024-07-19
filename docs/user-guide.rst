.. _User Guide:

User Guide
==========

This guide provides instructions on how to use the Flask application with the Flask-TUI-Editor.


.. _Installation:

Installation
############
To install Flask-TUI-Editor:

..  code-block:: text

    pip install flask-tui-editor


Basic Usage
###########

First, register the :py:class:`TUIEditor <flask_tui_editor.ext.TUIEditor>` class with Flask to load the necessary JavaScript and CSS files.

Next, include the `{{ flask_tui_editor.css }}` and `{{ flask_tui_editor.js }}` tags in the appropriate Jinja2 blocks within your HTML template.

Toast UI plugins and localizations are not loaded by default. You must specify which plugins and locales to load in the :py:class:`TUIEditor <flask_tui_editor.ext.TUIEditor>` class, as shown below:

.. code-block:: python

    ...
    app = Flask(__name__)
    TUIEditor(app, translations=["locale1", "locale2"], plugins=["plugin1", "plugin2"])
    ...

To integrate the editor into a Flask-WTF form, use the :py:class:`TUIEditorField <flask_tui_editor.fields.TUIEditorField>` class. You can customize the editor's appearance and behavior using the `editor_options` parameter.

For instance, the following code sets the editor's language to Turkish and the theme to dark:

.. code-block:: text

    {{ form.editor_field(editor_options='{"theme":"dark", "language":"tr"}') }}

Refer to the `Toast UI Editor documentation <https://nhn.github.io/tui.editor/latest/>`_ for a comprehensive list of configuration options available for the `editor_options` parameter, plugins and localizations.


Example project
###########

Example project is accessible at `example` directory in project folder.

**Project Structure:**

    .. code-block:: text

        example/
        ├── app.py
        ├── forms.py
        ├── templates/
            └── editor.html


**Files:**

*app.py*

..  code-block:: python

    from flask import Flask, render_template, request

    from flask_tui_editor import TUIEditor
    from forms import ContentDemoForm

    app = Flask(__name__)
    flask_tui_editor = TUIEditor(app, translations=["tr"])
    app.secret_key = 'your_secret_key'  # Replace with your actual secret key


    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = ContentDemoForm()
        if form.is_submitted():
            if form.validate_on_submit():
                content = form.content.data
                return f'Content: {content}'
        else:
            form.content.data = """
    # Heading 1

    ## Heading 2

    ### Heading 3

    #### Heading 4

    ##### Heading 5

    ###### Heading 6


    <br>
    ***

    **bold**
    *italic*
    ~~strikethrough~~

    ***

    <br>
    Unordered list:

    * item 1
    * item 2
    * item 3


    Ordered list:

    1. item 1
    2. item 2
    3. item 3


    ***
            """
        return render_template('editor.html', form=form)


    if __name__ == '__main__':
        app.run(debug=True)



*forms.py*

..  code-block:: python

    from flask_wtf import FlaskForm
    from wtforms import SubmitField
    from flask_tui_editor import TUIEditorField


    class ContentDemoForm(FlaskForm):
        content = TUIEditorField('Content', editor_options='{"theme":"dark", "language":"tr"}')
        submit = SubmitField('Submit')


*editor.html*

..  code-block:: html

    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Toast UI Editor Integration</title>
        {{ flask_tui_editor.css }}
    </head>
    <body>
        <form method="POST">
            {{ form.hidden_tag() }}
            <div>
                {{ form.content.label }}
                {{ form.content(editor_options='{"theme":"dark", "language":"tr"}') }}
            </div>
            <div>
                {{ form.submit() }}
            </div>
        </form>

        {{ flask_tui_editor.js }}
    </body>
    </html>

