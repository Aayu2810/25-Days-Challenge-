from typing import Any

# 1. Hover over print to see the original signature
def custom_print(*values: Any,
                 sep: str | None = " ",
                 end: str | None = "\n",
                 caps: bool = False,
                 include_types: bool = False) -> None:

    # Uppercases all string values if flag is toggled
    new_values: list[Any] = []
    for value in values:
        if isinstance(value, str) and caps:
            new_values.append(value.upper())
        else:
            new_values.append(value)

    # Includes type of every argument if flag is toggled
    values_with_type: list[Any] = []
    if include_types:
        for value in new_values:
            values_with_type.append((value, type(value)))

        print(*values_with_type, sep=sep, end=end)
    else:
        print(*new_values, sep=sep, end=end)


# 2. Have fun with custom printing!
custom_print('Bob', 'James', 10, caps=False, include_types=False, sep=', ')
custom_print('Bob', 'James', 10, caps=True, include_types=False, sep=', ', end='!\n')
custom_print('Bob', 'James', 10, include_types=True, sep=', ', end='!\n')
custom_print([], include_types=True, sep=', ', end='!\n')


# Homework:
# 1. Add a field that counts the number of elements being printed.
# 2. Add your very own feature to the custom print function.

