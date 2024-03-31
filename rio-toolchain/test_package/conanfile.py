from io import StringIO
from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain", "VirtualBuildEnv"

    def build_requirements(self):
        self.tool_requires(self.tested_reference_str)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run("arm-frc2024-linux-gnueabi-gcc --version")
        test_file = os.path.join(self.cpp.build.bindirs[0], "test_package")
        stdout = StringIO()
        self.run(f"file {test_file}", stdout=stdout)
        assert "ELF 32-bit" in stdout.getvalue()
