from conan import ConanFile
from conan.tools.files import get


class kauailabsRecipe(ConanFile):
    name = "kauailabs"
    version = "2023.0.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def requirements(self):
        self.requires("wpilibc/2023.4.3", transitive_headers=True, transitive_libs=True)

    def build(self):
        kauailabs_header_url, kauailabs_lib_url = super().generate_kauailabs_url(
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            str(self.options.shared),
            str(self.settings.build_type)
        )
        get(self, kauailabs_header_url)
        get(self, kauailabs_lib_url)
