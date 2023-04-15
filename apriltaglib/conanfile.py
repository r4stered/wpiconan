from conan import ConanFile
from conan.tools.files import get


class apriltaglibRecipe(ConanFile):
    name = "apriltaglib"
    version = "3.2.0-4"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def build(self):
        header_url, lib_url = super().generate_apriltag_url(
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            str(self.settings.build_type),
        )
        get(self, header_url)
        get(self, lib_url)
