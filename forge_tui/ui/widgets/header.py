from rich.text import Text
from textual.widget import Widget


class ForgeHeader(Widget):
    def __init__(
        self,
        title: str = "λ Lambda Forge",
        subtitle: str = "Simplify AWS Lambda deployments",
    ):
        self.title = title
        self.subtitle = subtitle

    def render(self):
        title = Text(self.title, style="bold")
        subtitle = Text(self.subtitle, style="dim")

        return title + "\n" + subtitle
