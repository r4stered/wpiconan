from conan import ConanFile
from conan.tools.files import get


class pathplannerRecipe(ConanFile):
    name = "pathplanner"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpilibnewcommands/2023.4.3", transitive_headers=True, transitive_libs=True)

    def build(self):
        pathplanner_header_url, pathplanner_lib_url = super().generate_pathplanner_url(
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            self.options.shared,
            str(self.settings.build_type)
        )
        get(self, pathplanner_header_url)
        get(self, pathplanner_lib_url)
