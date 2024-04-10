from conan import ConanFile
from conan.tools.files import copy
import os


class Wpibase:
    def get_os_name_for_url(self, os):
        return {"Windows": "windows", "Linux": "linux", "Macos": "osx"}.get(str(os))

    def get_arch_name_for_url(self, arch):
        return {
            "x86_64": "x86-64",
            "armv7": "arm32",
            "armv8": "arm64",
            "athena": "athena",
        }.get(str(arch))

    def get_shared_name_for_url(self, shared):
        if shared:
            return ""
        else:
            return "static"

    def get_build_type_name_for_url(self, build_type):
        if build_type == "Debug":
            return "debug"
        else:
            return ""

    def get_wpi_urls(self, lib_name, version, os, arch, shared, build_type):
        _os = self.get_os_name_for_url(os)
        _arch = self.get_arch_name_for_url(arch)
        _shared = self.get_shared_name_for_url(shared)
        _build_type = self.get_build_type_name_for_url(build_type)
        if _os == "osx":
            _arch = "universal"

        base_url = f"https://frcmaven.wpi.edu/artifactory/release/edu/wpi/first/{lib_name}/{lib_name}-cpp/{version}"
        header_url = f"{base_url}/{lib_name}-cpp-{version}-headers.zip"
        lib_url = f"{base_url}/{lib_name}-cpp-{version}-{_os}{_arch}{_shared}{_build_type}.zip"
        return (header_url, lib_url)

    def copy_common_files(self):
        copy(
            self, "*.h", self.build_folder, os.path.join(self.package_folder, "include")
        )
        copy(
            self,
            "*.hpp",
            self.build_folder,
            os.path.join(self.package_folder, "include"),
        )
        copy(
            self,
            "*.inc",
            self.build_folder,
            os.path.join(self.package_folder, "include"),
        )
        copy(
            self,
            "*.so.debug",
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
            "*.dll",
            self.build_folder,
            os.path.join(self.package_folder, "bin"),
            False,
        )
        copy(
            self,
            "*.pdb",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )


class WpiReq(ConanFile):
    name = "wpireq"
    version = "0.1"
    package_type = "python-require"
