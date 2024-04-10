from conan import ConanFile
from conan.tools.files import get


class NtcoreConan(ConanFile):
    name = "ntcore"
    version = "2024.3.2"
    settings = "os", "arch", "build_type"
    options = {"shared": [True, False]}
    python_requires = "wpireq/0.1"
    python_requires_extend = "wpireq.Wpibase"

    def requirements(self):
        self.requires(f"wpiutil/{self.version}")
        self.requires(f"wpinet/{self.version}")

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

    def package_info(self):
        if self.settings.os == "Windows" and self.settings.build_type == "Debug":
            lib_postfix = "d"
        else:
            lib_postfix = ""
        self.cpp_info.libs = [f"ntcore{lib_postfix}"]
