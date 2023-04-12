from conan import ConanFile
from conan.tools.files import get, copy, collect_libs
import os


class wpiutilRecipe(ConanFile):
    name = "wpiutil"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    # Optional metadata
    license = "https://github.com/wpilibsuite/allwpilib/blob/main/LICENSE.md"
    author = "Drew Williams williams.r.drew@gmail.com"
    url = "https://github.com/r4stered/wpiconan"
    description = "Repackage of wpiutil library; a part of allwpilib. See https://github.com/r4stered/allwpilib for source."
    topics = ("robotics", "frc", "utility")

    # Binary configuration
    settings = "os", "build_type", "arch"
    options = {"shared": [True, False], "target": [None, "ANY"]}
    default_options = {"shared": True}

    def build(self):
        header_url, lib_url = super().generate_download_urls(
            self.name,
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            self.options.shared,
            str(self.settings.build_type),
        )
        get(self, header_url)
        get(self, lib_url)

    def package(self):
        copy(
            self, "*.h", self.build_folder, os.path.join(self.package_folder, "include")
        )
        copy(
            self,
            "*.lib",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            "*.a",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            "*.so",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            "*.dylib",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            "*.dll",
            self.build_folder,
            os.path.join(self.package_folder, "bin"),
            False,
        )

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
