from textual.app import ComposeResult
from textual.widgets import Input, Select, TextArea
from ._base import TriggerBaseWidget


class ApiGateway(TriggerBaseWidget):
    DEFAULT_CSS = """
    ApiGateway {
        layout: grid;
        grid-size: 3 3;
        grid-rows: 5 10 auto;
    }

    ApiGateway > #url {
        column-span: 2;
    }
    """

    METHODS = ["GET", "POST", "PUT", "DELETE", "PATCH"]

    def compose(self) -> ComposeResult:
        yield Select(options=[(i, i) for i in self.METHODS], id="method")
        yield Input(id="url")
        yield TextArea.code_editor(text="{}", language="json", id="query")
        yield TextArea.code_editor(text="{}", language="json", id="body")
        yield TextArea.code_editor(text="{}", language="json", id="headers")
