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


def extract_after_slash(input_string):
    parts = input_string.split("/")
    return parts[1] if len(parts) > 1 else input_string


# venv_name = "./venv/bin/" if os.name == "posix" else "./venv/Scripts/"
# CI doenst need venv
venv_name = ""
conan_exec = venv_name + "conan"
pip_exec = venv_name + "pip"

# if not os.path.isdir("venv"):
#     print("Virtual env folder not found... creating one for you.")
#     if os.name == "posix":
#         subprocess.run(["python3", "-m", "venv", "./venv"])
#     else:
#         subprocess.run(["python", "-m", "venv", "./venv"])
#     subprocess.run([pip_exec, "install", "-r", "requirements.txt"])
# else:
#     print("Virtual env folder already exists, continuing.")

print("Installing conan settings.yml to include Rio arch")
subprocess.run([conan_exec, "config", "install", "config/settings.yml"])

print("Creating common package.")
subprocess.run([conan_exec, "create", "./wpicommon", f"--profile:all=./config/local"])

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

password = os.environ["CONAN_PASS"]
subprocess.run([conan_exec, "remote", "login", "-p", password, "team2053", "drew"])

for package in packages_to_build:
    for build_type in ["dbg", "rel"]:
        for shared in ["shared", "static"]:
            if package == "ntcoreffi" and shared == "static":
                continue

            if (
                package == "thirdparty/apriltaglib"
                or package == "thirdparty/googletest"
                or package == "thirdparty/imgui"
                or package == "thirdparty/libssh"
            ) and shared == "shared":
                continue

            print(f"Building {package} + {build_type} + {shared}...")
            retVal = subprocess.run(
                [
                    conan_exec,
                    "create",
                    f"./{package}",
                    f"--profile:all=./config/local-{build_type}-{shared}",
                ]
            ).returncode
            if retVal != 0:
                exit(1)
    subprocess.run(
        [conan_exec, "upload", extract_after_slash(f"{package}"), "-r=team2053"]
    )
