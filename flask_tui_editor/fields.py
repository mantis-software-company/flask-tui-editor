from wtforms import Field
from .widgets import TUIEditorWidget


class TUIEditorField(Field):
    """
    TUIEditorField(label=None, validators=None, editor_options='{}', **kwargs)

    A form field with a TUI editor widget.

    Args:
        label (str, optional): The label for the field.
        validators (list, optional): A sequence of validators to use.
        editor_options (str, optional): JSON string of options for the editor. Defaults to empty json string2.
        **kwargs: Additional keyword arguments.

    """

    widget = TUIEditorWidget()

    def __init__(self, label=None, validators=None, editor_options='{}', **kwargs):
        super().__init__(label, validators, **kwargs)

    def _value(self):
        return self.data if self.data else ''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0]
        else:
            self.data = None
