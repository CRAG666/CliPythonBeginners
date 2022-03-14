#!/usr/bin/env python3
from typing import Union
import argparse
from collections.abc import Sequence


command_without_args: dict[str, str] = {
    "subcommand1": "Ayuda con el subcomando",
    "subcommand2": "Ayuda con el subcomando",
    "subcommand3": "Ayuda con el subcomando",
    "subcommand4": "Ayuda con el subcomando",
}

command_needs_args: dict[str, dict[str, Union[str, dict[str, str]]]] = {
    "subcommand": {
        "help": "Ayuda con el subcomando que recibe parametros",
        "args": {
            "-d": "Ayuda para una bandera",
            "-c": "Ayuda para una bandera",
        },
    }
}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command, help in command_without_args.items():
        subparsers.add_parser(command, help=help)

    for command, meta in command_needs_args.items():
        command_parser = subparsers.add_parser(command, help=meta["help"])
        for argument, help in meta["args"].items():
            command_parser.add_argument(argument, nargs="?", help=help)

    args = parser.parse_args(argv)
    if args.command in command_without_args.keys():
        return call_without_args(args.command)
    elif args.command in command_needs_args.keys():
        dict_args = vars(args)
        return call_with_args(
            args.command,
            *tuple(
                filter(
                    lambda v: v is not None,
                    map(
                        lambda k: dict_args.get(k, None),
                        command_needs_args[args.command]["args"].keys(),
                    ),
                )
            ),
        )
    else:
        raise NotImplementedError(
            f"Command {args.command} does not exist.",
        )


def call_without_args(command: str) -> int:
    print(command)
    return 0


def call_with_args(command: str, *args) -> int:
    print(command, *args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
