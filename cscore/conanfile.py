from conan import ConanFile


class cscoreRecipe(ConanFile):
    name = "cscore"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpiutil/2023.4.3", transitive_headers=True)
        self.requires("wpinet/2023.4.3")
        self.requires("opencv/4.6.0-4")
