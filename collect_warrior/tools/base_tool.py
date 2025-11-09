from abc import ABC, abstractmethod
from typing import Any

class BaseTool(ABC):

    @abstractmethod
    def get_name(self) -> str:
        """The name of the tool"""

    @abstractmethod
    def get_description(self) -> str:
        """The description of the tool"""

    @abstractmethod
    def get_params(self) -> dict[str, Any]:
        """The parameters of the tool"""

    @abstractmethod
    def execute(self, **kwargs) -> dict[str, Any]:
        """Execute the tool"""

    def get_definition(self) -> dict[str, Any]:
        """The definition of the tool"""
        return {
            "name": self.get_name(),
            "description": self.get_description(),
            "params": self.get_params()
        }