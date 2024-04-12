import os
from conan import ConanFile
from conan.tools.files import get, copy


class WpimathConan(ConanFile):
    name = "wpimath"
    version = "2024.3.2"
    settings = "os", "arch", "build_type"
    options = {"shared": [True, False]}
    python_requires = "wpireq/0.1"
    python_requires_extend = "wpireq.Wpibase"

    def requirements(self):
        self.requires(f"wpiutil/{self.version}")

    def build(self):
        header_url, lib_url = super().get_wpi_urls(
            self.name,
            self.version,
            self.settings.os,
            self.settings.arch,
            self.options.shared,
            self.settings.build_type,
        )
        get(self, header_url)
        get(self, lib_url)

    def package(self):
        super().copy_common_files()
        # special case for Eigen files with no extension
        copy(
            self,
            "Eigen/*",
            self.build_folder,
            os.path.join(self.package_folder, "include"),
        )
        copy(
            self,
            "unsupported/*",
            self.build_folder,
            os.path.join(self.package_folder, "include"),
        )

    def package_info(self):
        if self.settings.build_type == "Debug":
            lib_postfix = "d"
        else:
            lib_postfix = ""
        self.cpp_info.libs = [f"wpimath{lib_postfix}"]
        if self.settings.os == "Windows":
            if self.settings.build_type == "Debug":
                self.cpp_info.cxxflags = ["/MDd"]
            if self.settings.build_type == "Release":
                self.cpp_info.cxxflags = ["/MD"]
