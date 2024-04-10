from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.build import can_run
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeToolchain", "CMakeDeps"

    def build_requirements(self):
        version = (self.tested_reference_str.split("/"))[1].split("#")[0]
        self.requires(f"wpiutil/{version}")
        self.requires(f"wpimath/{version}")
        self.requires(f"ntcore/{version}")
        self.requires(f"hal/{version}")
        self.requires(f"cscore/{version}")
        self.requires(f"cameraserver/{version}")
        self.requires(self.tested_reference_str)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if can_run(self):
            cmd = os.path.join(self.cpp.build.bindir, "test_package")
            self.run(cmd, env="conanrun")
