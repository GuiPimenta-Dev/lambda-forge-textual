from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container


class LambdaForge(App):
    BINDINGS = [
        ("s", "switch_to_server", "Server"),
        ("l", "switch_to_log", "Logs"),
        ("t", "switch_to_trigger", "Triggers"),
    ]

    CSS = """
    Screen {
        layout: vertical;
        height: 100%;
        width: 100%;
        border: solid purple;
    }
    
    Header {
        height: 3; 
        background: rgba(0, 0, 0, 0.5); 
        border: solid purple;
    }
    
    Footer {
        height: 3; 
        background: rgba(0, 0, 0, 0.5); 
        border: solid purple;
    }
    
    .main-container {
        layout: vertical;
        width: 100%;
        height: 100%;
    }
    
    .view {
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.1); 
    }
    
    .hidden {
        display: none;
    }
    
    .custom-live-log {
        layout: vertical;
        background: rgba(255, 255, 255, 0.1); 
        color: white; 
        border: solid green;
    }
    
    
    .custom-live-trigger {
        layout: vertical;
        background: rgba(255, 255, 255, 0.1); 
        color: white;  
        border: solid green;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(Static("Live Server", classes="view"), id="view-server")
        yield Container(Static("Live Log", classes="view "), id="view-log")
        yield Container(Static("Live Trigger", classes="view "), id="view-trigger")

    def on_mount(self) -> None:
        self.show_view("view-server")

    def action_switch_to_server(self) -> None:
        self.show_view("view-server")

    def action_switch_to_log(self) -> None:
        self.show_view("view-log")

    def action_switch_to_trigger(self) -> None:
        self.show_view("view-trigger")

    def action_toggle_dark_mode(self):
        self.dark = not self.dark
        self.refresh()

    def show_view(self, view_id: str) -> None:
        views = ["view-server", "view-log", "view-trigger"]
        for view in views:
            view_element = self.query_one(f"#{view}")
            if view == view_id:
                view_element.remove_class("hidden")
                if view == "view-log":
                    view_element.remove_class("view")
                    view_element.add_class("custom-live-log")
                elif view == "view-trigger":
                    view_element.remove_class("view")
                    view_element.add_class("custom-live-trigger")
                else:
                    view_element.add_class("view")
            else:
                view_element.add_class("hidden")
                view_element.remove_class("custom-live-log")
                view_element.remove_class("custom-live-trigger")
        self.refresh()


if __name__ == "__main__":
    LambdaForge().run()
