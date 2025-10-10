import configparser

from .settings import Setting, SettingBoolean


class Config(configparser.ConfigParser):
    def __init__(
        self,
        settings: dict[str, Setting],
        filename: str = "config.ini",
    ) -> None:
        super().__init__()

        self.settings = settings
        self.filename = filename

    def load(self):
        self.read(self.filename)

        for key, setting in self.settings.items():
            if isinstance(setting, SettingBoolean):
                setting.current_value = self.getboolean(
                    "SETTINGS", key, fallback=setting.default_value
                )
            else:
                setting.current_value = self.get(
                    "SETTINGS", key, fallback=setting.default_value
                )

    def save(self):
        for key, setting in self.settings.items():
            self["SETTINGS"] = {key: str(setting.current_value)}

        with open(self.filename, mode="w", encoding="utf-8") as configfile:
            self.write(configfile)

    def constant(self, name: str) -> str | None:
        return self.get("CONSTANTS", name, fallback=None)
