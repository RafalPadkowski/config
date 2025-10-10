import configparser

from .settings import Setting

DEFAULT_CONFIG_FILENAME = "config.ini"


class Config(configparser.ConfigParser):
    def __init__(
        self,
        settings: dict[str, Setting],
        filename: str = DEFAULT_CONFIG_FILENAME,
    ) -> None:
        super().__init__()

        self.settings = settings
        self.filename = filename

    def load(self):
        self.read(self.filename)

        for key, setting in self.settings.items():
            setting_value = self.get("SETTINGS", key, fallback=setting.default_value)
            setting.current_value = setting_value

    def save(self):
        pass
