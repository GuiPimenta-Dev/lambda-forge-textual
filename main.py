from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, Markdown
from server import Server

ROWS = [
    ("Name", "Service", "Type", "Trigger"),
    ("Live-Lambda-Forge-Demo-SecretAuthorizer", None, None, None),
    ("Live-Lambda-Forge-Demo-HelloWorld", "Api Gateway", "URL" ,"https://4hrnm139cf.execute-api.us-east-2.amazonaws.com/live/hello_world (GET)"),
    ("Live-Lambda-Forge-Demo-HelloAndre", "SNS", "ARN" ,"arn:aws:sns:us-east-2:211125768252:andre_topic"),
]

class Live(App):
    
    CSS_PATH = "styles.tcss"
    
    def __init__(self, rows, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = rows

    def compose(self) -> ComposeResult:
        with TabbedContent("Server", "Logs", "Triggers"):
            yield Server(self.rows)
            yield Markdown("Logs")
            yield Markdown("Triggers")



if __name__ == "__main__":
    Live(ROWS).run()
