from glob import glob
import dataclasses as dt
import typing as t
from pathlib import Path

import click
from click import Context, UsageError


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


CHAPTER_PREFIX = "chapter"
EXERCISE_PREFIX = "exercise"
WORKING_DIR = Path(__file__).parent


def unsafe(s: str, splitter="-") -> str:
    return s.replace(splitter, " ")


def safe(s: str, splitter="-") -> str:
    return s.replace(" ", splitter).lower()


@dt.dataclass
class Exercise:
    name: str
    number: int

    def __str__(self):
        return f"{self.number:02} {unsafe(self.name, '_')}"

    @property
    def file_name(self) -> str:
        return f"{EXERCISE_PREFIX}_{self.number:02}_{self.name}.py"


@dt.dataclass
class Chapter:
    name: str
    number: int

    exercises: t.Sequence[Exercise]

    def __str__(self):
        return f"{self.number:02} {unsafe(self.name)}"

    def last_exercise_no(self) -> int:
        try:
            return max(e.number for e in self.exercises)
        except ValueError:
            return 0

    @property
    def file_name(self) -> str:
        return f"{CHAPTER_PREFIX}-{self.number:02}-{self.name}"


def exercise_from_path(path: Path) -> Exercise:
    _, number, name = path.name.split("_", 2)
    return Exercise(number=int(number), name=name[: -(len(".py"))])


def chapter_from_path(path: Path) -> Chapter:
    _, number, name = path.name.split("-", 2)
    exercises = [
        exercise_from_path(Path(exercise))
        for exercise in glob(str(path / f"{EXERCISE_PREFIX}_*"))
    ]

    return Chapter(name=name, number=int(number), exercises=exercises)


def all_chapters(path: Path) -> list[Chapter]:
    return [
        chapter_from_path(path / file_name)
        for file_name in glob(str(path / f"{CHAPTER_PREFIX}-*"))
    ]


@click.group()
def cli():
    pass


@cli.group()
def chapter():
    """Manage chapters"""


@chapter.command("list")
def chapter_list():
    """List chapters"""
    for chapter in all_chapters(WORKING_DIR):
        print(f"Chapter: {color.BOLD}{chapter}{color.END}")

        for exercise in chapter.exercises:
            print(f" •  {color.BOLD}{exercise}{color.END}")


@chapter.command("add")
@click.argument("name", type=str)
def chapter_add(name: str):
    name = safe(name)
    number = current_chapter() + 1
    chapter = Chapter(name=safe(name), number=number, exercises=[])
    chapter_name = chapter.file_name
    click.echo(f"Adding chapter {color.BOLD}{chapter_name}{color.END}")
    (WORKING_DIR / chapter_name).mkdir()


def current_chapter() -> int:
    try:
        number = max(c.number for c in all_chapters(WORKING_DIR))
    except ValueError:
        number = 0
    return number


@cli.group()
@click.option("--chapter", type=int, help="Chapter number, last if not specified")
@click.pass_context
def exercise(ctx: Context, chapter: int | None):
    """
    Manipulate chapter exercises
    """
    ctx.ensure_object(dict)
    if not chapter:
        chapter = current_chapter()

    try:
        (ctx.obj["chapter"],) = (
            c for c in all_chapters(WORKING_DIR) if c.number == chapter
        )
    except ValueError:
        raise UsageError(f"Chapter {chapter} does not exists")
    return chapter


def exercise_content(exercise_name: str) -> str:
    exercise_name = safe(exercise_name, "_")
    return f"""\"\"\"
TODO: add description
\"\"\"
import pytest


def {exercise_name}(input):
    ...


@pytest.fixture(
    params=[
        {exercise_name},
    ]
)
def function_under_test(request):
    return request.param
    

@pytest.mark.parametrize(
    "input,expected",
    [
        ("foo", False),
    ],
)
def test_{exercise_name}(input, expected, function_under_test):
    assert function_under_test(input) == expected


if __name__ == "__main__":
    print(f"{{{exercise_name}('')=}}")
"""


@exercise.command("add")
@click.argument("name", type=str)
@click.pass_context
def exercise_add(ctx: Context, name):
    chapter = ctx.obj["chapter"]
    path = WORKING_DIR / chapter.file_name
    number = chapter.last_exercise_no() + 1

    exercise = Exercise(number=number, name=safe(name, "_"))
    exercise_name = exercise.file_name

    with open(path / exercise_name, "w") as f:
        f.write(exercise_content(name))


if __name__ == "__main__":
    cli()
