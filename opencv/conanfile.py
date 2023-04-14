from conan import ConanFile
from conan.tools.files import get, rename, collect_libs
import glob
import os


class opencvRecipe(ConanFile):
    name = "opencv"
    version = "4.6.0-4"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def build(self):
        header_url, lib_url = super().generate_opencv_url(
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            self.options.shared,
            str(self.settings.build_type),
        )
        get(self, header_url)
        get(self, lib_url)

    def package_info(self):

        if str(self.settings.os) == "Linux" and self.options.shared:
            libs = []
            for entry in os.scandir(os.path.join(self.package_folder, "lib")):
                print(entry.name)
                if not str(entry.name).endswith(".debug"):
                    libs.append(entry.name)
            self.cpp_info.libs = libs
        else:
            self.cpp_info.libs = collect_libs(self)
        print(self.cpp_info.libs)
