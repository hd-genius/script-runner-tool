from pathlib import Path
import subprocess
from runr.api import register_handler, ScriptHandler, Script


@register_handler
class PowershellHandler(ScriptHandler):
    def can_handle(self, file: Path) -> bool:
        return file.suffix == ".py"

    def create_script_for(self, file: Path) -> Script:
        return PythonScript(file)


class PythonScript(Script):
    def __init__(self, file: Path) -> None:
        super().__init__(file)

    def execute(self):
        subprocess.run(f"python {self.path}")
