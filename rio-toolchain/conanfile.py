import os
from conan import ConanFile
from conan.tools.files import get, copy
from conan.errors import ConanInvalidConfiguration
from conan.tools.scm import Version


class RioToolchainPackage(ConanFile):
    name = "rio-toolchain"
    version = "v2024-1"

    license = "GPL-3.0-only"
    homepage = "https://github.com/wpilibsuite/opensdk"
    description = "Conan package for the NI RoboRio, targeting all Tier 1 hosts listed on the github page."
    settings = "os", "arch"
    package_type = "application"
    toolchain_name = "arm-nilrt-linux-gnueabi"
    triplet_name = "arm-frc2024-linux-gnueabi"

    def _get_url_from_os(self):
        ext = ".tgz"
        if self.settings.os == "Windows":
            os_name = "w64-mingw32"
            ext = ".zip"
        if self.settings.os == "Macos":
            os_name = "apple-darwin"
        if self.settings.os == "Linux":
            os_name = "linux-gnu"

        if self.settings.arch == "x86_64":
            arch_name = "x86_64"
        if self.settings.arch == "armv8":
            arch_name = "arm64"
        return (os_name, arch_name, ext)

    def validate(self):
        if self.settings.arch == "x86_64":
            if (
                self.settings.os != "Linux"
                and self.settings.os != "Macos"
                and self.settings.os != "Windows"
            ):
                raise ConanInvalidConfiguration(
                    f"This toolchain is not compatible with {self.settings.os}-{self.settings.arch}. "
                    "It can only run on Windows x86-64, Mac x86-64, Mac ARMv8, and Linux x86-64"
                )
        elif self.settings.arch == "armv8":
            if self.settings.os != "Macos":
                raise ConanInvalidConfiguration(
                    f"This toolchain is not compatible with {self.settings.os}-{self.settings.arch}. "
                    "It can only run on Windows x86-64, Mac x86-64, Mac ARMv8, and Linux x86-64"
                )
        else:
            raise ConanInvalidConfiguration(
                f"This toolchain is not compatible with {self.settings.os}-{self.settings.arch}. "
                "It can only run on Windows x86-64, Mac x86-64, Mac ARMv8, and Linux x86-64"
            )

        if self.settings_target.os != "Linux" and self.settings_target.arch != "athena":
            raise ConanInvalidConfiguration(
                f"This toolchain only supports building for Linux-athena. "
                f"{self.settings_target.os}-{self.settings_target.arch} is not supported."
            )

        if self.settings_target.compiler != "gcc":
            raise ConanInvalidConfiguration(
                f"The compiler is set to '{self.settings_target.compiler}', but this "
                "toolchain only supports building with gcc."
            )

        if Version(self.settings_target.compiler.version) != "12.1":
            raise ConanInvalidConfiguration(
                f"Invalid gcc version '{self.settings_target.compiler.version}'. "
                "Only gcc 12.1 is supported."
            )

    def build(self):
        os_name, arch_name, ext = self._get_url_from_os()
        get(
            self,
            f"https://github.com/wpilibsuite/opensdk/releases/download/v2024-1/cortexa9_vfpv3-roborio-academic-2024-{arch_name}-{os_name}-Toolchain-12.1.0{ext}",
            strip_root=True,
        )

    def package(self):
        dirs_to_copy = [self.toolchain_name, "bin", "include", "lib", "libexec"]
        for dir_name in dirs_to_copy:
            root_folder = "roborio-academic/"
            if self.settings.os == "Windows":
                root_folder = ""
            copy(
                self,
                pattern=f"{root_folder}{dir_name}/*",
                src=self.build_folder,
                dst=self.package_folder,
                keep_path=True,
            )

    def package_id(self):
        self.info.settings_target = self.settings_target
        # We only want the ``arch and os`` setting
        self.info.settings_target.rm_safe("compiler")
        self.info.settings_target.rm_safe("build_type")

    def package_info(self):
        self.cpp_info.bindirs.append(
            os.path.join(self.package_folder, "roborio-academic", "bin")
        )

        ext = ""
        if self.settings_build.os == "Windows":
            ext = ".exe"

        self.conf_info.define(
            "tools.build:compiler_executables",
            {
                "c": f"{self.triplet_name}-gcc{ext}",
                "cpp": f"{self.triplet_name}-g++{ext}",
                "asm": f"{self.triplet_name}-as{ext}",
                "fortran": f"{self.triplet_name}-gfortran{ext}",
            },
        )

        if self.settings.os == "Windows":
            self.conf_info.define_path(
                "tools.build:sysroot",
                os.path.join(self.package_folder, self.toolchain_name, "sysroot"),
            )
        else:
            self.conf_info.define_path(
                "tools.build:sysroot",
                os.path.join(
                    self.package_folder,
                    "roborio-academic",
                    self.toolchain_name,
                    "sysroot",
                ),
            )
