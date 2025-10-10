from dataclasses import dataclass, field
from typing import Any


@dataclass
class Setting:
    label: str
    default_value: Any
    current_value: Any | None = None


@dataclass
class SettingOption:
    display_str: str
    value: Any


@dataclass
class SettingOptions(Setting):
    options: list[SettingOption] = field(default_factory=lambda: list[SettingOption]())


@dataclass
class SettingBoolean(Setting):
    current_value: bool | None = None
    default_value: bool
