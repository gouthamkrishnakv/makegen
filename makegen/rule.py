"""
Makegen: Rule Module

Copyright (C) 2023 Goutham Krishna K V 
"""


from typing import Any

from makegen.utils import render_recipe, render_rule


class Rule:
    """
    Rule

    This holds an abstract rule
    """

    target: str | list[str] | list[Any]
    prerequisites: str | list[str] | None
    # TODO: Switch to list[Recipe], which is commands/string, use class
    recipe: list[str | list[str]] | None

    def __init__(
        self, target: str | list[str], prerequisites: str | list[str] | None = None
    ) -> None:  # TODO: Add targets and pre-requisites properly here
        self.target = target
        self.prerequisites = prerequisites
        self.recipe = None

    def set_recipe(self, recipe: list[str | list[str]] | None = None):
        if recipe is not None:
            self.recipe = recipe

    def render(self):
        return (
            "\n".join(
                [render_rule(self.target, "world")]
                + list(
                    map(render_recipe, self.recipe) if self.recipe is not None else ""
                ),
            )
            + "\n"
        )
