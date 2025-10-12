import configparser
from dataclasses import fields, is_dataclass
from typing import Generic, TypeVar

from .settings import SettingBoolean

TUi = TypeVar("TUi")
TSettings = TypeVar("TSettings")


class Config(configparser.ConfigParser, Generic[TUi, TSettings]):
    def __init__(
        self,
        filename: str = "config.ini",
        ui: TUi | None = None,
        settings: TSettings | None = None,
    ) -> None:
        super().__init__()

        self.filename = filename

        self.ui = ui
        self.settings = settings

        self.load()

    def load(self):
        self.read(self.filename)

        if self.ui and is_dataclass(self.ui):
            for f in fields(self.ui):
                value = self.get("UI", f.name, fallback="")
                setattr(self.ui, f.name, value)

        if self.settings is not None and is_dataclass(self.settings):
            for f in fields(self.settings):
                setting = getattr(self.settings, f.name)
                if isinstance(setting, SettingBoolean):
                    setting.current_value = self.getboolean(
                        "SETTINGS", f.name, fallback=setting.default_value
                    )
                else:
                    setting.current_value = self.get(
                        "SETTINGS", f.name, fallback=setting.default_value
                    )

    def save_settings(self):
        if self.settings is not None and is_dataclass(self.settings):
            if not self.has_section("SETTINGS"):
                self.add_section("SETTINGS")

            for f in fields(self.settings):
                setting = getattr(self.settings, f.name)
                self.set("SETTINGS", f.name, str(setting.current_value))

            with open(self.filename, mode="w", encoding="utf-8") as configfile:
                self.write(configfile)
