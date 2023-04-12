from conan import ConanFile
from conan.tools.files import get


class opencvRecipe(ConanFile):
    name = "opencv"
    version = "4.6.0-4"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def build(self):
        header_url, lib_url = super().generate_opencv_url(
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            self.options.shared,
            str(self.settings.build_type),
        )
        get(self, header_url)
        get(self, lib_url)
