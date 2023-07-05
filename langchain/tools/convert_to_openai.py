from typing import TypedDict

from langchain.tools import BaseTool, StructuredTool


class FunctionDescription(TypedDict):
    """Representation of a callable function to the OpenAI API."""

    name: str
    """The name of the function."""
    description: str
    """A description of the function."""
    parameters: dict
    """The parameters of the function."""


def format_tool_to_openai_function(tool: BaseTool) -> FunctionDescription:
    """Format tool into the OpenAI function API."""
    if isinstance(tool, BaseTool):
        properties = tool.args
        return {
            "name": tool.name,
            "description": tool.description,
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": sorted(properties),
            },
        }
