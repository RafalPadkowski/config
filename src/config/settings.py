from dataclasses import dataclass
from typing import Any


@dataclass
class Setting:
    label: str
    default_value: Any
    current_value: Any


@dataclass
class SettingOption:
    display_str: str
    value: Any


@dataclass
class SettingOptions(Setting):
    options: list[SettingOption]


@dataclass
class SettingBoolean(Setting):
    current_value: bool
    default_value: bool
