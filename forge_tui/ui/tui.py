from textual.app import App
from .widgets import LogStream, ServerTable, Triggers
from .screens import IndexScreen


class ForgeTUI(App):
    SCREENS = {
        "index": IndexScreen(),
    }

    def on_mount(self) -> None:
        self.push_screen("index")
