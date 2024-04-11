#!/usr/bin/env python3

import subprocess
import os
from itertools import chain


def contains_subdirectory_with_os_scandir(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir() and entry.name == "test_package":
                return True
    return False


if not os.path.isdir("venv"):
    print("Virtual env folder not found... creating one for you.")
    subprocess.run(["python3", "-m", "venv", "./venv"])
    subprocess.run(["./venv/bin/pip", "install", "-r", "requirements.txt"])
else:
    print("Virtual env folder already exists, continuing.")

print("Installing conan settings.yml to include Rio arch")
subprocess.run(["./venv/bin/conan", "config", "install", "profiles/settings.yml"])

print("Creating common package.")
subprocess.run(["./venv/bin/conan", "create", "./wpicommon"])

print("Creating list of packages to create..")

directory = "thirdparty"
print(contains_subdirectory_with_os_scandir(directory))

print("Creating native packages.")
packages_to_build = [
    "thirdparty/apriltaglib",
    "thirdparty/googletest",
    "thirdparty/imgui",
    "thirdparty/libssh",
    "thirdparty/opencv",
    "wpigui",
    "wpiutil",
    "wpimath",
    "apriltag",
    "wpinet",
    "hal",
    "ntcore",
    "ntcoreffi",
    "cscore",
    "cameraserver",
    "wpilibc",
    "wpilibnewcommands",
]

for package in packages_to_build:
    for build_type in ["dbg", "rel"]:
        for shared in ["shared", "static"]:

            if package == "ntcoreffi" and shared == "static":
                continue

            print(f"Building {package} + {build_type} + {shared}...")
            retVal = subprocess.run(
                [
                    "./venv/bin/conan",
                    "create",
                    f"./{package}",
                    f"--profile:all=./profiles/local-{build_type}-{shared}",
                ]
            ).returncode
            if retVal != 0:
                exit(1)
