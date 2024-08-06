from textual.app import App
from .screens import IndexScreen, LoadingScreen


class ForgeTUI(App):
    SCREENS = {
        "index": IndexScreen(),
        "loader": LoadingScreen(),
    }
    CSS_PATH = "styles.css"

    def on_mount(self) -> None:
        self.push_screen("loader")
