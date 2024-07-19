from markupsafe import Markup
from wtforms.widgets import html_params


class TUIEditorWidget:
    """
    TUIEditorWidget()

    A widget for rendering a Toast UI Editor in a form field.

    Methods:
        __call__(field, editor_options='{}', **kwargs):
            Renders the widget as HTML.

    """

    def __call__(self, field, editor_options='{}', **kwargs):
        """
        Renders the widget as HTML.

        Args:
            field (Field): The form field to which the widget is attached.
            editor_options (str, optional): JSON string of options for the editor. Defaults to '{}'.
            **kwargs: Additional keyword arguments for HTML attributes.

        Returns:
            Markup: The rendered HTML for the widget.
        """
        kwargs.setdefault('id', field.id)
        html = f"""
        <div {html_params(name=field.name, **kwargs)}></div>
        <input type="hidden" name="{field.name}" id="{field.id}_hidden" value="{field._value()}">
        <script>
         document.addEventListener("DOMContentLoaded", function() {{
            initializeToastUIEditor('{field.id}', '{field.id}_hidden', {editor_options});
         }});
        </script>
        """
        return Markup(html.strip())
