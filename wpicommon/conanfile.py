from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.build import can_run
from conan.tools.files import copy, get, collect_libs
import os
from conan.errors import ConanInvalidConfiguration


class WpiCommon:

    # Optional metadata
    license = "https://github.com/wpilibsuite/allwpilib/blob/main/LICENSE.md"
    author = "Drew Williams williams.r.drew@gmail.com"
    url = "https://github.com/r4stered/wpiconan"
    description = "Repackage of wpiutil library; a part of allwpilib. See https://github.com/r4stered/allwpilib for source."
    topics = ("robotics", "frc", "utility")

    # Binary configuration
    settings = "os", "build_type", "arch"
    options = {"shared": [True, False], "target": [None, "ANY"]}
    default_options = {"shared": True}

    def generate_download_urls(self, library_name, version, os, arch, shared, debug):
        _os = {"Windows": "windows", "Linux": "linux", "Macos": "osx"}.get(os)
        _arch = arch.lower().replace("_", "-")
        _debug = debug.lower()

        if _os == "osx":
            _arch = "universal"

        if _os == "linux" and arch == "armv7":
            _arch = "athena"

        if _os == "linux" and arch == "armv6":
            _arch = "arm32"

        base_url = f"https://frcmaven.wpi.edu/artifactory/release/edu/wpi/first/{library_name}/{library_name}-cpp/{version}/{library_name}-cpp-{version}-"
        header_url = base_url + "headers.zip"

        static_str = "" if shared else "static"
        debug_str = "debug" if _debug == "debug" else ""

        lib_url = base_url + f"{_os}{_arch}{static_str}{debug_str}.zip"

        return (header_url, lib_url)

    def build(self):
        header_url, lib_url = super().generate_download_urls(
            self.name,
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            self.options.shared,
            str(self.settings.build_type),
        )
        get(self, header_url)
        get(self, lib_url)

    def package(self):
        copy(
            self, "*.h", self.build_folder, os.path.join(self.package_folder, "include")
        )
        copy(
            self,
            "*.lib",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            "*.a",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            "*.so",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            "*.dylib",
            self.build_folder,
            os.path.join(self.package_folder, "lib"),
            False,
        )
        copy(
            self,
            "*.dll",
            self.build_folder,
            os.path.join(self.package_folder, "bin"),
            False,
        )

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)


class testPackageBase:
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if can_run(self):
            cmd = os.path.join(self.cpp.build.bindir, "test_exec")
            self.run(cmd, env="conanrun")


class toolchainPackageBase:
    package_type = "application"
    options = {"target": [None, "ANY"]}
    default_options = {"target": None}
    # Binary configuration
    settings = "os", "build_type", "arch"
    temp_package_folder = None

    def get_toolchain_url(self, target_arch, build_os, build_arch, version):
        # TODO: delicate version name
        target_arch_str = ""
        version_str = "10.2.0"
        if str(target_arch) == "armv8":
            target_arch_str = "arm64-bullseye-2023"
        if str(target_arch) == "armv7hf":
            target_arch_str = "armhf-bullseye-2023"
        if str(target_arch) == "armv6":
            target_arch_str = "armhf-raspi-bullseye-2023"
        if str(target_arch) == "armv7":
            target_arch_str = "cortexa9_vfpv3-roborio-academic-2023"
            version_str = "12.1.0"

        build_os_str = ""
        ext_str = "tgz"
        if str(build_os) == "Windows":
            build_os_str = "w64-mingw32"
            ext_str = "zip"
        if str(build_os) == "Macos":
            build_os_str = "apple-darwin"
        if str(build_os) == "Linux":
            build_os_str = "linux-gnu"

        return (
            f"https://github.com/wpilibsuite/opensdk/releases/download/{version}/{target_arch_str}-{build_arch}-{build_os_str}-Toolchain-{version_str}.{ext_str}",
        )

    def validate(self):
        settings_target = getattr(self, "settings_target", None)
        if settings_target is None:
            print("Running as host")
            # It is running in 'host', so Conan is compiling this package
            if not self.options.target:
                raise ConanInvalidConfiguration(
                    "A value for option 'target' has to be provided"
                )
        else:
            print("Running as compiler")
            if self.options.target:
                raise ConanInvalidConfiguration(
                    "Value for the option 'target' will be computed from settings_target"
                )
            print("self.settings_target.arch: " + str(self.settings_target.arch))
            self.options.target = self.settings_target.arch
            if not (
                str(self.options.target) == "armv8"
                or str(self.options.target) == "armv7hf"
                or str(self.options.target) == "armv6"
                or str(self.options.target) == "armv7"
            ):
                raise ConanInvalidConfiguration(
                    "Target arch not supported: " + str(self.options.target)
                )

    def package(self):
        copy(self, "*", self.build_folder, self.package_folder)

    def package_info(self):
        if self.temp_package_folder is not None:
            with open(os.path.join(self.package_folder, "conan_toolchain.cmake")) as f:
                s = f.read()
                if self.temp_package_folder not in s:
                    print(
                        '"{self.temp_package_folder}" not found in conan_toolchain.cmake.'.format(
                            **locals()
                        )
                    )
                    return

            # Safely write the changed content, if found in the file
            with open(
                os.path.join(self.package_folder, "conan_toolchain.cmake"), "w"
            ) as f:
                print(
                    'Changing "{self.temp_package_folder}" to "{self.package_folder}" in conan_toolchain.cmake'.format(
                        **locals()
                    )
                )
                s = s.replace(
                    self.temp_package_folder,
                    str(self.package_folder).replace(os.sep, "/"),
                )
                f.write(s)

        f = os.path.join(self.package_folder, "conan_toolchain.cmake")
        self.conf_info.define("tools.cmake.cmaketoolchain:user_toolchain", [f])


class WpiCommonPkg(ConanFile):
    name = "wpicommon"
    version = "0.1"
    package_type = "python-require"
