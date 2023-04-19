from conan import ConanFile
from conan.tools.files import get


class revRecipe(ConanFile):
    name = "rev"
    version = "2023.1.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpilibc/2023.4.3", transitive_headers=True, transitive_libs=True)

    def build(self):
        revcpp_header_url, revcpp_lib_url = super().generate_rev_url(
            "cpp",
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            self.options.shared,
            str(self.settings.build_type)
        )
        get(self, revcpp_header_url)
        get(self, revcpp_lib_url)

        revdriver_header_url, revdriver_lib_url = super().generate_rev_url(
            "driver",
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            str(self.options.shared),
            str(self.settings.build_type)
        )
        get(self, revdriver_header_url)
        get(self, revdriver_lib_url)
