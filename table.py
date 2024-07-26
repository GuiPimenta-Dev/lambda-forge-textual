from rich.console import Console
from rich.table import Table

functions = [
    {
        "name": "Live-Lambda-Forge-Demo-HelloWorld",
        "triggers": "https://4hrnm139cf.execute-api.us-east-2.amazonaws.com/live/hello_world",
    },
    {"name": "Live-Lambda-Forge-Demo-SecretAuthorizer", "triggers": ""},
]


class LiveServer:
    def show_table(self, functions):
      table = Table(title="Live Server")

      table.add_column("Name", justify="right", style="cyan", no_wrap=True)
      table.add_column("Triggers", style="magenta")
      
      for function in functions:
        table.add_row(function["name"], function["triggers"])

      console = Console()
      console.print(table)



LiveServer().show_table(functions)
