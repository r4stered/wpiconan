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

        os.chdir(self.build_folder)
        for file in glob.glob("**/*.4.6", recursive=True):
            print("Old file name:")
            print(file)
            new_file_name = file.replace(".4.6", "")
            print("New file name")
            print(new_file_name)
            new_file_name = file.replace(".4.6", "")
            rename(self, file, new_file_name)

        for file in glob.glob("**/*.4.6.debug", recursive=True):
            print("Old file name:")
            print(file)
            new_file_name = file.replace(".4.6.debug", "")
            print("New file name")
            print(new_file_name)
            rename(self, file, new_file_name)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
