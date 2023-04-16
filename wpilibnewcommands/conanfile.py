from conan import ConanFile


class wpilibnewcommandsRecipe(ConanFile):
    name = "wpilibnewcommands"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpilibc/2023.4.3", transitive_headers=True, transitive_libs=True)