from conan import ConanFile
from conan.tools.files import get, copy
import os


class NilibrariesConan(ConanFile):
    name = "nilibraries"
    version = "2024.2.1"
    settings = "build_type"
    python_requires = "wpireq/0.1"
    python_requires_extend = "wpireq.Wpibase"

    def build(self):
        chipobject_header_url, chipobject_lib_url = super().get_ni_urls(
            "chipobject",
            self.version,
            self.settings.build_type,
        )
        get(self, chipobject_header_url)
        get(self, chipobject_lib_url)

        netcomm_header_url, netcomm_lib_url = super().get_ni_urls(
            "netcomm",
            self.version,
            self.settings.build_type,
        )
        get(self, netcomm_header_url)
        get(self, netcomm_lib_url)

        _, runtime_lib_url = super().get_ni_urls(
            "runtime",
            self.version,
            self.settings.build_type,
        )
        get(self, runtime_lib_url)

        visa_header_url, visa_lib_url = super().get_ni_urls(
            "visa",
            self.version,
            self.settings.build_type,
        )
        get(self, visa_header_url)
        get(self, visa_lib_url)

    def package(self):
        super().copy_common_files()
        copy(
            self,
            "*.so.*",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )

    def package_info(self):
        self.cpp_info.libs = [
            "libRoboRIO_FRC_ChipObject.so.24.0.0",
            "libFRC_NetworkCommunication.so.24.0.0",
            "libembcanshim.so",
            "libfpgalvshim.so",
            "libvisa.so.23.3.0",
        ]
