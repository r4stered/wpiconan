import os
from conan import ConanFile
from conan.tools.files import get, copy


class WpimathConan(ConanFile):
    name = "libssh"
    version = "0.105-1"
    settings = "os", "arch", "build_type"
    python_requires = "wpireq/0.1"
    python_requires_extend = "wpireq.Wpibase"

    def build(self):
        _os = self.get_os_name_for_url(self.settings.os)
        _arch = self.get_arch_name_for_url(self.settings.arch)
        _build_type = self.get_build_type_name_for_url(self.settings.build_type)
        if _os == "osx":
            _arch = "universal"

        base_url = f"https://frcmaven.wpi.edu/artifactory/release/edu/wpi/first/thirdparty/frc2024/{self.name}/{self.version}"
        header_url = f"{base_url}/{self.name}-{self.version}-headers.zip"
        lib_url = (
            f"{base_url}/{self.name}-{self.version}-{_os}{_arch}static{_build_type}.zip"
        )

        get(self, header_url)
        get(self, lib_url)

    def package(self):
        copy(
            self, "*.h", self.build_folder, os.path.join(self.package_folder, "include")
        )
        copy(
            self,
            "*.a",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )

    def package_info(self):
        self.cpp_info.libs = [f"ssh{self.version}"]
