from textual import on, events
from textual.app import ComposeResult
from textual.widgets import Static, Select, Label, TextArea, Input, Button

QUERY = """\
{
  
}
"""

HEADERS = """\
{
  
}
"""

BODY = """\
{
  
}
"""


class ApiGateway(Static):
    method = "GET"
    url = ""
    query = QUERY
    headers = HEADERS
    body = BODY
    

    def compose(self) -> ComposeResult:
        methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
        options = ((method, method) for method in methods)

        yield Select(options=options, value="GET")
        yield Input(placeholder="First Name")
        yield Label("Query:")
        yield TextArea.code_editor(self.body, id="query")
        yield Label("Headers:")
        yield TextArea.code_editor(self.headers, id="headers")
        yield Label("Body:")
        yield TextArea.code_editor(self.body, id="body")
        yield Button(label="Submit", variant="primary")
        self.result_label = Label("")
        yield self.result_label

    @on(Input.Changed)
    def input_changed(self, event: Input.Changed) -> None:
        self.url = event.value
        self.input=event.value

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.method = str(event.value)

    @on(TextArea.Changed)
    def textarea_changed(self, event: TextArea.Changed) -> None:
        if event.text_area.id == "query":
            self.query = event.text_area.text
        elif event.text_area.id == "headers":
            self.headers = event.text_area.text
        elif event.text_area.id == "body":
            self.body = event.text_area.text


    @on(Button.Pressed)
    def submit_pressed(self, event: Button.Pressed) -> None:
        result = (
            f"Method: {self.method}\n"
            f"URL: {self.url}\n"
            f"Query: {self.query}\n"
            f"Headers: {self.headers}\n"
            f"Body: {self.body}\n"
        )
        self.result_label.update(result)

