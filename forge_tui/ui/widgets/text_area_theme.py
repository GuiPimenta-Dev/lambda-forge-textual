from rich.style import Style
from textual.widgets.text_area import TextAreaTheme

nord_theme = TextAreaTheme(
    name="nord",
    cursor_style=Style(color="#d8dee9", bgcolor="#2e3440"),
    cursor_line_style=Style(bgcolor="#ebcb8b"),
)
