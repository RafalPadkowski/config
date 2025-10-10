from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Setting(Generic[T]):
    label: str
    default_value: T
    current_value: T

    def __init__(self, label: str, default_value: T, current_value: T | None = None):
        self.label = label
        self.default_value = default_value
        self.current_value = (
            current_value if current_value is not None else default_value
        )


@dataclass
class SettingOption:
    display_str: str
    value: str | int


@dataclass
class SettingOptions(Setting[str | int]):
    options: list[SettingOption]

    def __init__(
        self,
        label: str,
        options: list[SettingOption],
        default_value: str | int,
        current_value: str | int | None = None,
    ):
        super().__init__(label, default_value, current_value)
        self.options = options


@dataclass
class SettingBoolean(Setting[bool]):
    pass
