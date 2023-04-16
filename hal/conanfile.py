from conan import ConanFile
from conan.tools.files import collect_libs


class halRecipe(ConanFile):
    name = "hal"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        if self.options.target == "armv7":
            self.requires("nilibraries/2023.3.0", transitive_headers=True, transitive_libs=True)
        self.requires("wpiutil/2023.4.3", transitive_headers=True, transitive_libs=True)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        if str(self.settings.os) == "Linux":
            self.cpp_info.system_libs = ["pthread", "dl"]