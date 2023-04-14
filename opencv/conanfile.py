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
        for entry in os.scandir(os.path.join(self.build_folder, str(self.settings.os).lower(), str(self.settings.arch).replace("_", "-"), "shared" if self.options.shared else "static")):
            print(entry.path)
            final_name = str(entry.path).replace(".4.6", "").replace(".debug", "")
            print(final_name)
            if not str(entry.path).endswith(".so"):
                rename(self, entry.path, final_name)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        print(self.cpp_info.libs)
