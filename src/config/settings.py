from dataclasses import dataclass, field
from typing import Generic, TypeVar, Union

TValue = TypeVar("TValue")


@dataclass
class Setting(Generic[TValue]):
    label: str
    default_value: TValue
    current_value: TValue = field(init=False)
    old_value: TValue = field(init=False)

    @property
    def changed(self) -> bool:
        return self.current_value != self.old_value


@dataclass
class SettingOption:
    display_str: str
    value: str


@dataclass
class SettingOptions(Setting[str]):
    default_value: str
    current_value: str
    old_value: str
    options: list[SettingOption]


@dataclass
class SettingBoolean(Setting[bool]):
    default_value: bool
    current_value: bool
    old_value: bool


SettingType = Union[SettingOptions, SettingBoolean]
