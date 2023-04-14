from conan import ConanFile
from conan.tools.files import collect_libs


class ntcoreRecipe(ConanFile):
    name = "ntcore"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpiutil/2023.4.3", transitive_headers=True, transitive_libs=True)
        self.requires("wpinet/2023.4.3", transitive_headers=True, transitive_libs=True)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        if str(self.settings.os) == "Linux":
            self.cpp_info.system_libs = ["pthread", "dl"]
