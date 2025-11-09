"""
Base Tool Interface

Defines the standard interface for all tools in the system.
All tools should inherit from this base class and implement the required methods.
"""


class BaseToolInterface:
    """
    Abstract base class for all tools.

    This class defines the standard interface that all tools must implement:
    - get_name: Returns the tool's name
    - get_description: Returns a description of what the tool does
    - get_parameter: Returns information about a specific parameter
    - get_definition: Returns the complete parameter definitions
    - execute: Executes the tool with given parameters
    """

    def get_name(self) -> str:
        """
        Get the name of the tool.

        Returns:
            str: The name of the tool
        """
        raise NotImplementedError("Subclasses must implement get_name()")

    def get_description(self) -> str:
        """
        Get a description of what the tool does.

        Returns:
            str: A description of the tool's functionality
        """
        raise NotImplementedError("Subclasses must implement get_description()")

    def get_parameter(self, parameter_name: str) -> dict:
        """
        Get information about a specific parameter.

        Args:
            parameter_name (str): The name of the parameter

        Returns:
            dict: Parameter information (e.g., type, description, required, default)

        Raises:
            KeyError: If the parameter doesn't exist
        """
        raise NotImplementedError("Subclasses must implement get_parameter()")

    def get_definition(self) -> dict:
        """
        Get the complete parameter definitions for the tool.

        Returns:
            dict: A dictionary containing all parameter definitions,
                  where keys are parameter names and values are parameter metadata
        """
        raise NotImplementedError("Subclasses must implement get_definition()")

    def execute(self, **kwargs) -> any:
        """
        Execute the tool with the given parameters.

        Args:
            **kwargs: Parameters to pass to the tool

        Returns:
            any: The result of executing the tool

        Raises:
            ValueError: If required parameters are missing or invalid
        """
        raise NotImplementedError("Subclasses must implement execute()")


# Example of how to use this base class:
"""
from base_tool_interface import BaseToolInterface

class ExampleTool(BaseToolInterface):
    def get_name(self):
        return "example_tool"

    def get_description(self):
        return "This is an example tool that demonstrates the interface"

    def get_parameter(self, parameter_name):
        definition = self.get_definition()
        if parameter_name not in definition:
            raise KeyError(f"Parameter '{parameter_name}' not found")
        return definition[parameter_name]

    def get_definition(self):
        return {
            "input_text": {
                "type": "str",
                "description": "Text to process",
                "required": True,
                "default": None
            },
            "count_words": {
                "type": "bool",
                "description": "Whether to count words in the text",
                "required": False,
                "default": False
            }
        }

    def execute(self, **kwargs):
        input_text = kwargs.get("input_text")
        count_words = kwargs.get("count_words", False)

        if input_text is None:
            raise ValueError("Parameter 'input_text' is required")

        if count_words:
            word_count = len(input_text.split())
            return f"Text length: {len(input_text)} characters, {word_count} words"
        else:
            return f"Text length: {len(input_text)} characters"
"""