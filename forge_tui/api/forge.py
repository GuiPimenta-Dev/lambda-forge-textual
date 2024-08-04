from pathlib import Path
from typing import List, Optional


class Forge:
    def get_servers(self) -> List[List[Optional[str]]]:
        ROWS = [
            ("Live-Lambda-Forge-Demo-SecretAuthorizer", None, None, None),
            (
                "Live-Lambda-Forge-Demo-HelloWorld",
                "Api Gateway",
                "URL",
                "https://4hrnm139cf.execute-api.us-east-2.amazonaws.com/live/hello_world (GET)",
            ),
            (
                "Live-Lambda-Forge-Demo-HelloAndre",
                "SNS",
                "ARN",
                "arn:aws:sns:us-east-2:211125768252:andre_tqopic",
            ),
        ]
        return ROWS

    def get_log_path(self) -> Path:
        return Path(__file__).parent.parent.parent / "old" / "live.log"
