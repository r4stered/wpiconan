from conan import ConanFile


class halRecipe(ConanFile):
    name = "hal"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpiutil/2023.4.3", transitive_headers=True, transitive_libs=True)
