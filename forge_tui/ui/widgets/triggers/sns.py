from textual.app import ComposeResult
from textual.widgets import Input, TextArea
from ._base import TriggerBaseWidget, TriggerBaseContainer


class SNSContainer(TriggerBaseContainer):
    DEFAULT_CSS = """
    SNSContainer {
        layout: grid;
        grid-size: 2 2;
        grid-rows: 5 10;
        grid-columns: 1fr 1fr;

        Input {
            column-span: 2;
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Input(id="topic_arn")
        yield TextArea.code_editor(text="{}", language="json", id="message")
        yield TextArea.code_editor(text="{}", language="json", id="subject")


class SNS(TriggerBaseWidget):
    def render_left(self) -> ComposeResult:
        yield SNSContainer()
