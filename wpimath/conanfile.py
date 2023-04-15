from conan import ConanFile
import os
from conan.tools.files import copy


class wpimathRecipe(ConanFile):
    name = "wpimath"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpiutil/2023.4.3", transitive_headers=True, transitive_libs=True)

    def package(self):
        for root, dirs, files in os.walk(self.build_folder):
            for filename in files:
                (name, ext) = os.path.splitext(filename)
                if not ext:
                    print(f"file {name} doesnt have an extension.. Copying to build folder")
                    print(root)
                    print(name)
                    copy(self, os.path.relpath(os.path.join(root, name), self.build_folder), self.build_folder, os.path.join(self.package_folder, "include"))
        super().package()
