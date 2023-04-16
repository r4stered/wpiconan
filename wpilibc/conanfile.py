from conan import ConanFile


class wpilibcRecipe(ConanFile):
    name = "wpilibc"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("cameraserver/2023.4.3", transitive_headers=True, transitive_libs=True)
        self.requires("hal/2023.4.3", transitive_headers=True, transitive_libs=True)
        self.requires("ntcore/2023.4.3", transitive_headers=True, transitive_libs=True)
        self.requires("cscore/2023.4.3", transitive_headers=True, transitive_libs=True)
        self.requires("wpimath/2023.4.3", transitive_headers=True, transitive_libs=True)
        self.requires("wpiutil/2023.4.3", transitive_headers=True, transitive_libs=True)