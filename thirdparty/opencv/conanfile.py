import os
from conan import ConanFile
from conan.tools.files import get, copy


class OpencvConan(ConanFile):
    name = "opencv"
    version = "4.8.0-2"
    settings = "os", "arch", "build_type"
    options = {"shared": [True, False]}
    python_requires = "wpireq/0.1"
    python_requires_extend = "wpireq.Wpibase"

    def build(self):
        _os = self.get_os_name_for_url(self.settings.os)
        _arch = self.get_arch_name_for_url(self.settings.arch)
        _shared = self.get_shared_name_for_url(self.options.shared)
        _build_type = self.get_build_type_name_for_url(self.settings.build_type)
        if _os == "osx":
            _arch = "universal"

        base_url = f"https://frcmaven.wpi.edu/artifactory/release/edu/wpi/first/thirdparty/frc2024/{self.name}/{self.name}-cpp/{self.version}"
        header_url = f"{base_url}/{self.name}-cpp-{self.version}-headers.zip"
        lib_url = f"{base_url}/{self.name}-cpp-{self.version}-{_os}{_arch}{_shared}{_build_type}.zip"

        get(self, header_url)
        get(self, lib_url)

    def package(self):
        version_postfix = self.version[0:3]
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
            "*.so.debug",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            f"*.so.{version_postfix}",
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

    def package_info(self):
        if self.options.shared:
            collected_libs = []
            for f in os.listdir(os.path.join(self.package_folder, "lib")):
                if f.endswith(".4.8"):
                    if f.startswith("lib"):
                        print(f)
                        collected_libs.append(f)
            self.cpp_info.libs = collected_libs
        else:
            self.cpp_info.libs = [f"opencv{self.version[:5].replace('.', '')}"]
