from rich.style import Style
from textual.widgets.text_area import TextAreaTheme
from textual.widgets import TextArea

nord_theme = TextAreaTheme(
    name="nord",
    cursor_style=Style(color="#2e3440", bgcolor="#d8dee9"),
    cursor_line_style=Style(bgcolor="#3b4252"),
)


def get_text_area(_id: str) -> TextArea:
    w = TextArea.code_editor(text="{}", language="json", id=_id)
    w.register_theme(nord_theme)
    w.theme = "nord"
    return w
