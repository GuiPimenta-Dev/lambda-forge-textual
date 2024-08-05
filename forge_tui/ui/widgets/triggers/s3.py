from textual.app import ComposeResult
from textual.widgets import Input, TextArea
from ._base import TriggerBaseWidget, TriggerBaseContainer


class S3Container(TriggerBaseContainer):
    DEFAULT_CSS = """
    S3Container {
        layout: grid;
        grid-size: 2 3;
        grid-rows: 5 10 auto;
        grid-columns: 1fr 1fr;

        TextArea {
            column-span: 2;
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Input(id="bucket_name")
        yield Input(id="file_path")
        yield TextArea.code_editor(text="{}", language="json", id="metadata")


class S3(TriggerBaseWidget):
    def render_left(self) -> ComposeResult:
        yield S3Container()
