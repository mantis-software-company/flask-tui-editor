from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_tui_editor import TUIEditorField


class ContentDemoForm(FlaskForm):
    content = TUIEditorField('Content', editor_options='{"theme":"dark", "language":"tr"}')
    submit = SubmitField('Submit')
