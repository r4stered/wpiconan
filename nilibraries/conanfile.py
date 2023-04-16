from conan import ConanFile
from conan.tools.files import copy, get, collect_libs


class nilibrariesRecipe(ConanFile):
    name = "nilibraries"
    version = "2023.3.0"
    # Optional metadata
    license = "https://github.com/wpilibsuite/allwpilib/blob/main/LICENSE.md"
    author = "Drew Williams williams.r.drew@gmail.com"
    url = "https://github.com/r4stered/wpiconan"
    description = "Repackage of allwpilib. See https://github.com/r4stered/allwpilib for source."
    topics = ("robotics", "frc", "utility")

    # Binary configuration
    settings = "build_type"
    options = {"shared": [True, False], "target": [None, "ANY"]}

    def generate_nilib_urls(self, library_name, version, debug):
        _debug = debug.lower()

        base_url = f"https://frcmaven.wpi.edu/artifactory/release/edu/wpi/first/ni-libraries/{library_name}/{version}/{library_name}-{version}-"
        header_url = base_url + "headers.zip"

        debug_str = "debug" if _debug == "debug" else ""

        lib_url = base_url + f"linuxathena{debug_str}.zip"

        return (header_url, lib_url)

    def build(self):
        chipobj_header_url, chipobj_lib_url = self.generate_nilib_urls(
            "chipobject",
            self.version,
            str(self.settings.build_type),
        )
        get(self, chipobj_header_url)
        get(self, chipobj_lib_url)

        netcomm_header_url, netcomm_lib_url = self.generate_nilib_urls(
            "netcomm",
            self.version,
            str(self.settings.build_type),
        )
        get(self, netcomm_header_url)
        get(self, netcomm_lib_url)

        runtime_header_url, runtime_lib_url = self.generate_nilib_urls(
            "runtime",
            self.version,
            str(self.settings.build_type),
        )
        get(self, runtime_header_url)
        get(self, runtime_lib_url)

        visa_header_url, visa_lib_url = self.generate_nilib_urls(
            "visa",
            self.version,
            str(self.settings.build_type),
        )
        get(self, visa_header_url)
        get(self, visa_lib_url)

    def package(self):
        copy(
            self, "*.h", self.build_folder, os.path.join(self.package_folder, "include")
        )
        copy(
            self, "*.inc", self.build_folder, os.path.join(self.package_folder, "include")
        )
        copy(
            self, "*.hpp", self.build_folder, os.path.join(self.package_folder, "include")
        )
        copy(
            self,
            "*.so",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
