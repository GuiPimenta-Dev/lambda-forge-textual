from textual.app import ComposeResult
from textual.widgets import Input, Select, TextArea
from ._base import TriggerBaseWidget


class ApiGatewayContainer(TriggerBaseWidget):
    DEFAULT_CSS = """
    ApiGatewayContainer {
        layout: grid;
        grid-size: 3 3;
        grid-rows: 5 10 auto;
        grid-columns: 1fr 1fr 1fr;
    }

    ApiGatewayContainer > #url {
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


class ApiGateway(TriggerBaseWidget):
    def render_left(self) -> ComposeResult:
        yield ApiGatewayContainer()
