def sort_authors(authors: list) -> list:
    return sorted(authors, key=lambda x: x.split()[-1].upper())


def sort_authors2(authors: list) -> list:
    def surname(author: str) -> str:
        return author.split()[-1].upper()

    return sorted(authors, key=surname)


# print(sort_authors2(["J. K. Rowling", "w. s.", "lewis carroll", "M. M."]))
# print(sort_authors2(["J. L.", "J. B. priestley", "L. C.", "Suzanne Collins"]))

assert sort_authors(["J. K. Rowling", "w. s.", "lewis carroll", "M. M."]) == [
    "lewis carroll",
    "M. M.",
    "J. K. Rowling",
    "w. s.",
]
assert sort_authors(["J. L.", "J. B. priestley", "L. C.", "Suzanne Collins"]) == [
    "L. C.",
    "Suzanne Collins",
    "J. L.",
    "J. B. priestley",
]
