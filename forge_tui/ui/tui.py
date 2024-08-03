from textual.app import App
from .screens import IndexScreen


class ForgeTUI(App):
    SCREENS = {
        "index": IndexScreen(),
    }

    def on_mount(self) -> None:
        self.push_screen("index")
