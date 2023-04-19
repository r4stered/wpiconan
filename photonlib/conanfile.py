from conan import ConanFile
from conan.tools.files import get


class photonlibRecipe(ConanFile):
    name = "photonlib"
    version = "2023.4.2"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpilibc/2023.4.3", transitive_headers=True, transitive_libs=True)

    def build(self):
        photonlib_header_url, photonlib_lib_url = super().generate_photonlib_url(
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            self.options.shared,
            str(self.settings.build_type)
        )
        get(self, photonlib_header_url)
        get(self, photonlib_lib_url)
