#! /usr/bin/env python3
class Sandwich:
    def __init__(self, bread: str = "", ingredients: list = []) -> None:
        self.bread = bread
        self.ingredients = ingredients

    def describe(self):
        return f"""
You've got a sandwich made of: {self.bread} and filled out with:
{",\n".join(self.ingredients)}
"""


class BreadOptions:
    def __init__(self) -> None:
        self.options = []

    def add_option(self, option: str):
        self.options.append(option)
        return self

    def get_options(self):
        return self.options


class SandwichBuilder:
    def __init__(self, bread_options: BreadOptions) -> None:
        self.sandwich = Sandwich()
        self.bread_options = bread_options.get_options()

    def bread_option(self, option: str):
        try:
            choice = self.bread_options.index(option)
            self.sandwich.bread = self.bread_options[choice]
        except ValueError as e:
            raise e
        return self

    def add_ingredient(self, ingredient: str):
        self.sandwich.ingredients.append(ingredient)

        return self

    def build(self):
        return self.sandwich


def main():
    regular_bread_options = [
        "white bread",
        "whole wheat",
        "sourdough",
        "baggette",
        "ciabatta",
    ]
    bread_options = BreadOptions()

    for bread in regular_bread_options:
        bread_options.add_option(bread)

    regular_sandwich = SandwichBuilder(bread_options)

    regular_sandwich.bread_option("white bread").add_ingredient("ham").add_ingredient(
        "lettuce"
    ).add_ingredient("mushrooms")

    print(regular_sandwich.build().describe())


if __name__ == "__main__":
    main()
