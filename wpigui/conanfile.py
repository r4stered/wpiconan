from conan import ConanFile
from conan.tools.files import get


class WpiguiConan(ConanFile):
    name = "wpigui"
    version = "2024.3.2"
    settings = "os", "arch", "build_type"
    python_requires = "wpireq/0.1"
    python_requires_extend = "wpireq.Wpibase"

    def requirements(self):
        self.requires("imgui/1.89.9-1")

    def build(self):
        header_url, lib_url = super().get_wpi_urls(
            self.name,
            self.version,
            self.settings.os,
            self.settings.arch,
            False,
            self.settings.build_type,
        )
        get(self, header_url)
        get(self, lib_url)

    def package(self):
        super().copy_common_files()

    def package_info(self):
        self.cpp_info.libs = ["wpigui"]
