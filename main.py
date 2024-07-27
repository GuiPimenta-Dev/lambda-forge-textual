from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, Markdown, Footer, TabPane
from logs import Logs
from server import Server
from textual.binding import Binding

ROWS = [
    ("Live-Lambda-Forge-Demo-SecretAuthorizer", None, None, None),
    ("Live-Lambda-Forge-Demo-HelloWorld", "Api Gateway", "URL" ,"https://4hrnm139cf.execute-api.us-east-2.amazonaws.com/live/hello_world (GET)"),
    ("Live-Lambda-Forge-Demo-HelloAndre", "SNS", "ARN" ,"arn:aws:sns:us-east-2:211125768252:andre_tqopic"),
]

class Live(App):
    
    BINDINGS = [
        Binding("s", "show_tab('server')", "Server", show=False),
        Binding("l", "show_tab('logs')", "Logs", show=False),
        Binding("t", "show_tab('triggers')", "Trigger", show=False),
    ]
    def __init__(self, rows, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = rows

    def compose(self) -> ComposeResult:
        yield Footer()
        with TabbedContent():
            
            with TabPane("Server", id="server"):
                yield Server(self.rows)
            
            with TabPane("Logs", id="logs"):
                yield Logs("live.log")
            
            with TabPane("Triggers", id="triggers"):
                yield Markdown("Triggers")
                
    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab

if __name__ == "__main__":
    Live(ROWS).run()
