#! /usr/bin/env python3

from typing import List, Optional, Self


class Sandwich:
    def __init__(
        self, bread: str = "", ingredients: Optional[List[str]] = None
    ) -> None:
        self.bread = bread
        self.ingredients = ingredients or []

    def describe(self):
        filled = ",\n".join(self.ingredients) if self.ingredients else "nothing"
        bread_type = self.bread or "no bread selected"

        return f"""
You've got a sandwich made of: a {bread_type} and filled out with:
{filled}"""


class BreadOptions:
    def __init__(self) -> None:
        self.options = []

    def add_option(self, option: str) -> Self:
        self.options.append(option)
        return self

    def get_options(self) -> List[str]:
        return self.options[:]


class SandwichBuilder:
    def __init__(self, bread_options: BreadOptions) -> None:
        self.sandwich = Sandwich()
        self.bread_options = bread_options.get_options()

    def bread_option(self, option: str) -> Self:
        if option not in self.bread_options:
            raise ValueError(
                f"{option} is not available, choose from {self.bread_options}"
            )

        self.sandwich.bread = option
        return self

    def add_ingredient(self, ingredient: str) -> Self:
        self.sandwich.ingredients.append(ingredient)

        return self

    def build(self) -> Sandwich:
        if not self.sandwich.bread or not self.sandwich.ingredients:
            missing = "bread is" if not self.sandwich.bread else "ingredients are"

            raise ValueError(f"The {missing} missing from this order")
        return self.sandwich

    def reset(self) -> Self:
        self.sandwich = Sandwich()
        return self


def main():
    regular_bread_options = [
        "white bread",
        "whole wheat",
        "sourdough",
        "baguette",
        "ciabatta",
    ]
    bread_options = BreadOptions()

    for bread in regular_bread_options:
        bread_options.add_option(bread)

    regular_sandwich = SandwichBuilder(bread_options)

    sandwich = (
        regular_sandwich.bread_option("white bread")
        .add_ingredient("ham")
        .add_ingredient("lettuce")
        .add_ingredient("mushrooms")
        .build()
    )

    print(sandwich.describe())

    regular_sandwich.reset()

    another_sandwich = (
        regular_sandwich.bread_option("baguette")
        .add_ingredient("cheese")
        .add_ingredient("ham")
        .add_ingredient("pepper")
        .build()
    )

    print(another_sandwich.describe())


if __name__ == "__main__":
    main()
