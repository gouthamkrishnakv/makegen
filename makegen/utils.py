"""
Makegen: Utilities

Copyright (C) 2023 Goutham Krishna K V
"""

from string import Template

DEFAULT_COLON = ":"

RULE_TEMPLATE = "$targets $colon $prerequisites"

RECIPE_TEMPLATE = "\t$recipe"


def render_rule(targets: str | list[str], prerequisites: str | list[str] | None) -> str:
    targets_str, prereqs_str = "", ""
    if isinstance(targets, str):
        targets_str = targets
    elif isinstance(targets, list):
        targets_str = " ".join(targets)
    if prerequisites is not None:
        if isinstance(prerequisites, str):
            prereqs_str = prerequisites
        if isinstance(prerequisites, list):
            prereqs_str = " ".join(prerequisites)
    return Template(RULE_TEMPLATE).safe_substitute(
        targets=targets_str, prerequisites=prereqs_str, colon=DEFAULT_COLON
    )


def render_recipe(recipe: list[str] | str) -> str:
    recipe_str = ""
    if isinstance(recipe, str):
        recipe_str = recipe
    elif isinstance(recipe, list):
        recipe_str = " ".join(recipe)
    return Template(RECIPE_TEMPLATE).safe_substitute(recipe=recipe_str)
