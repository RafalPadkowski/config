import tomllib
from dataclasses import fields, is_dataclass
from typing import Any, ClassVar, Final, Protocol, Type

from .settings import SettingBoolean, SettingOption, SettingOptions, SettingType

CONFIG_FILENAME: Final[str] = "config.toml"


class Dataclass(Protocol):
    __dataclass_fields__: ClassVar[dict[str, Any]]


def load_config(
    ui_cls: Type[Dataclass] | None = None,
    settings_cls: Type[Dataclass] | None = None,
) -> tuple[Dataclass | None, Dataclass | None, dict[str, Any]]:
    with open(CONFIG_FILENAME, mode="rb") as file:
        config_dict = tomllib.load(file)

    if is_dataclass(ui_cls):
        ui = ui_cls(**config_dict["ui"])
    else:
        ui = None

    if is_dataclass(settings_cls):
        settings_values: dict[str, Any] = {}

        for field in fields(settings_cls):
            setting: SettingType

            if field.type is SettingOptions:
                d = config_dict["settings"][field.name]
                options = [
                    SettingOption(**option)
                    for option in config_dict["settings"][field.name]["options"]
                ]
                setting = SettingOptions(
                    **{k: v for k, v in d.items() if k != "options"}, options=options
                )
            else:
                setting = SettingBoolean(**config_dict["settings"][field.name])

            settings_values[field.name] = setting

        settings = settings_cls(**settings_values)
    else:
        settings = None

    return ui, settings, config_dict


def save_settings():
    if self.settings is not None and is_dataclass(self.settings):
        if not self.has_section("SETTINGS"):
            self.add_section("SETTINGS")

        for f in fields(self.settings):
            setting = getattr(self.settings, f.name)
            self.set("SETTINGS", f.name, str(setting.current_value))

        with open(self.filename, mode="w", encoding="utf-8") as configfile:
            self.write(configfile)
