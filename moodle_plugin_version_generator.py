#!/usr/bin/env python3

import datetime
# import os
from os import environ, chdir

VERSION_MATCH = "$plugin->version"

def get_version_line():
    with open("version.php", "r") as a_file:
        list_of_lines = a_file.readlines()

    for i, line in enumerate(list_of_lines):
        if line.find(VERSION_MATCH) != -1:
            print(f"Found {VERSION_MATCH} at line {i}")
            print(f"{line}")
            return i


def get_current_version(line):
    print("Retrieve the current version")

    with open("version.php", "r") as a_file:
        list_of_lines = a_file.readlines()

    version_line = list_of_lines[line].split(";")[0]
    current_version = version_line.split("=")[1].replace(" ","")
    return current_version


def increase_version(current_version):
    print("Increase the current version")

    version_date = current_version[0:8]
    version_number = current_version[8:]
    version_number_len = len(version_number)
    current_date = datetime.datetime.now().strftime("%Y%m%d")

    print("Current version date " + version_date)
    print("Current version number " + version_number)
    print(f"version_date={version_date}")
    print(f"current_date={current_date}")

    if current_date == version_date:
        version_number = int(version_number) + 1
    else:
        print("Increase the current version date and reset version number to 00")
        version_date = current_date
        version_number = "0"

    version_number = str(version_number).zfill(version_number_len)
    new_version = f"{version_date}{version_number}"

    print("New version date " + version_date)
    print("New version number " + version_number)

    return new_version


def overwrite_version(line, new_version):
    print("Overwrite the current version in the file")

    with open("version.php", "r") as a_file:
        list_of_lines = a_file.readlines()

    list_of_lines[line] = "$plugin->version = " + new_version + ";\n"

    with open("version.php", "w") as a_file:
        a_file.writelines(list_of_lines)


def main():

    # raises an exception if the env var doesn't exist
    chdir(environ['INPUT_PATH'])

    line = get_version_line()
    print(f"line={line}")
    if line:
        current_version = get_current_version(line)
        print(f"current_version={current_version}")
        new_version = increase_version(current_version)
        print(f"new_version={new_version}")
        overwrite_version(line, new_version)
    else:
        print(f"{VERSION_MATCH} not found")


if __name__ == "__main__":
    main()
