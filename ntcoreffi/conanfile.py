from conan import ConanFile
from conan.tools.files import get


class NtcoreffiConan(ConanFile):
    name = "ntcoreffi"
    version = "2024.3.2"
    settings = "os", "arch", "build_type"
    options = {"shared": [True, False]}
    python_requires = "wpireq/0.1"
    python_requires_extend = "wpireq.Wpibase"

    def requirements(self):
        self.requires(f"ntcore/{self.version}")

    def build(self):
        _, lib_url = super().get_wpi_urls(
            self.name,
            self.version,
            self.settings.os,
            self.settings.arch,
            self.options.shared,
            self.settings.build_type,
        )
        get(self, lib_url)

    def package(self):
        super().copy_common_files()

    def package_info(self):
        # ffi doesnt have headers
        self.cpp_info.includedirs = []
        self.cpp_info.libs = ["ntcoreffi"]
        if self.settings.os == "Windows":
            if self.settings.build_type == "Debug":
                self.cpp_info.cxxflags = ["/MDd"]
            if self.settings.build_type == "Release":
                self.cpp_info.cxxflags = ["/MD"]
