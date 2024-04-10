from conan import ConanFile
from conan.tools.files import get


class FieldImagesConan(ConanFile):
    name = "fieldimages"
    version = "2024.3.2"
    settings = "os", "arch", "build_type"
    options = {"shared": [True, False]}
    python_requires = "wpireq/0.1"
    python_requires_extend = "wpireq.Wpibase"

    def build(self):
        header_url, lib_url = super().get_wpi_urls(
            self.name,
            self.version,
            self.settings.os,
            self.settings.arch,
            self.options.shared,
            self.settings.build_type,
        )

        header_url = header_url.replace("fieldimages", "fieldImages")
        lib_url = lib_url.replace("fieldimages", "fieldImages")

        get(self, header_url)
        get(self, lib_url)

    def package(self):
        super().copy_common_files()
