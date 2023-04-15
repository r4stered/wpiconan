from conan import ConanFile


class apriltagRecipe(ConanFile):
    name = "apriltag"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("apriltaglib/3.2.0-4", transitive_headers=True, transitive_libs=True)
        self.requires("wpimath/2023.4.3", transitive_headers=True, transitive_libs=True)
