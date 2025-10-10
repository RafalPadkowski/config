from dataclasses import dataclass, field
from typing import Any


@dataclass
class Setting:
    label: str
    default_value: Any
    current_value: Any = field(init=False)

    def __post_init__(self) -> None:
        self.current_value = self.default_value


@dataclass
class SettingOption:
    display_str: str
    value: str | int


@dataclass
class SettingOptions(Setting):
    default_value: str | int
    current_value: str | int
    options: list[SettingOption]


@dataclass
class SettingBoolean(Setting):
    default_value: bool
    current_value: bool
