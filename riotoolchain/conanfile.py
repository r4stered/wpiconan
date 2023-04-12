import os
from conan import ConanFile
from conan.tools.files import get
from conan.tools.cmake import CMakeToolchain


class riotoolchainRecipe(ConanFile):
    name = "riotoolchain"
    version = "v2023-8"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.toolchainPackageBase"

    def generate(self):
        self.temp_package_folder = str(self.package_folder).replace(os.sep, "/")
        toolchain_url = super().get_toolchain_url(
            self.options.target,
            self.settings_build.os,
            self.settings_build.arch,
            self.version,
        )
        get(self, toolchain_url)

        ext_str = ""
        if str(self.settings_build.os) == "Windows":
            ext_str = ".exe"

        bin_folder = os.path.join(
            self.package_folder, "roborio-academic", "bin"
        ).replace(os.sep, "/")

        tc = CMakeToolchain(self)
        tc.variables["CMAKE_SYSTEM_NAME"] = "Linux"
        tc.variables["CMAKE_SYSTEM_VERSION"] = "1"
        tc.variables["CMAKE_SYSTEM_PROCESSOR"] = "arm"
        tc.variables["CMAKE_SYSROOT"] = os.path.join(
            self.package_folder,
            "roborio-academic",
            "arm-nilrt-linux-gnueabi",
            "sysroot",
        ).replace(os.sep, "/")
        if str(self.settings_build.os) != "Windows":
            tc.variables["CMAKE_C_FLAGS"] = "-Wno-psabi"
            tc.variables["CMAKE_CXX_FLAGS"] = "-Wno-psabi"
            tc.variables["CMAKE_Fortran_FLAGS"] = "-Wno-psabi"
        tc.variables["CMAKE_C_COMPILER"] = os.path.join(
            bin_folder, "arm-frc2023-linux-gnueabi-gcc" + ext_str
        ).replace(os.sep, "/")
        tc.variables["CMAKE_CXX_COMPILER"] = os.path.join(
            bin_folder, "arm-frc2023-linux-gnueabi-g++" + ext_str
        ).replace(os.sep, "/")
        tc.variables["CMAKE_Fortran_COMPILER"] = os.path.join(
            bin_folder, "arm-frc2023-linux-gnueabi-gfortran" + ext_str
        ).replace(os.sep, "/")
        tc.variables["CMAKE_AR"] = os.path.join(
            bin_folder, "arm-frc2023-linux-gnueabi-ar" + ext_str
        ).replace(os.sep, "/")
        tc.variables["CMAKE_AS"] = os.path.join(
            bin_folder, "arm-frc2023-linux-gnueabi-as" + ext_str
        ).replace(os.sep, "/")
        tc.variables["CMAKE_NM"] = os.path.join(
            bin_folder, "arm-frc2023-linux-gnueabi-nm" + ext_str
        ).replace(os.sep, "/")
        tc.variables["CMAKE_LINKER"] = os.path.join(
            bin_folder, "arm-frc2023-linux-gnueabi-ld" + ext_str
        ).replace(os.sep, "/")
        tc.variables["CMAKE_FIND_ROOT_PATH_MODE_PROGRAM"] = "NEVER"
        tc.variables["CMAKE_FIND_ROOT_PATH_MODE_LIBRARY"] = "ONLY"
        tc.variables["CMAKE_FIND_ROOT_PATH_MODE_INCLUDE"] = "ONLY"
        tc.variables["CMAKE_FIND_ROOT_PATH_MODE_PACKAGE"] = "ONLY"
        tc.generate()
