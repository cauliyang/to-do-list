import typing as t
from datetime import date

from jinja2 import Environment, FileSystemLoader


def read_todos():
    with open("todos/todo.md") as f:
        return [line.strip() for line in f.readlines()]


def clean_todos():
    with open("todos/todo.md", "w") as f:
        f.write("")


def generate_md(todos: t.List[str]) -> str:
    env = Environment(loader=FileSystemLoader("./todos"))
    template = env.get_template("template.md")
    return template.render(todos=todos, date=date.today(), count=len(todos))


def write_md(md: str) -> None:
    with open(f"./todos/{date.today()}.md", "w") as f:
        f.write(md)


def main():
    todos = read_todos()
    write_md(generate_md(todos))
    clean_todos()


if __name__ == "__main__":
    main()
