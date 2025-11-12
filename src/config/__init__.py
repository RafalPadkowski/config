import tomllib
from dataclasses import fields, is_dataclass
from typing import Final, Type, TypeVar, cast

from .settings import SettingBoolean

TUi = TypeVar("TUi")
TSettings = TypeVar("TSettings")


CONFIG_FILENAME: Final[str] = "config.toml"


def load_ui(ui_cls: Type[TUi]) -> TUi:
    if not is_dataclass(ui_cls):
        raise TypeError(f"{ui_cls} is not a dataclass")

    with open(CONFIG_FILENAME, mode="rb") as file:
        config_dict = tomllib.load(file)

    ui_values = [config_dict["ui"].get(field.name, "") for field in fields(ui_cls)]
    ui = cast(TUi, ui_cls(*ui_values))

    return ui


def load_settings(settings_cls: Type[TSettings]) -> TSettings:
    if is_dataclass(settings_cls):
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

    settings = settings_cls()

    return settings


def save_settings(self):
    if self.settings is not None and is_dataclass(self.settings):
        if not self.has_section("SETTINGS"):
            self.add_section("SETTINGS")

        for f in fields(self.settings):
            setting = getattr(self.settings, f.name)
            self.set("SETTINGS", f.name, str(setting.current_value))

        with open(self.filename, mode="w", encoding="utf-8") as configfile:
            self.write(configfile)
