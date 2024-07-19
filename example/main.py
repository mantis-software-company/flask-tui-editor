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
