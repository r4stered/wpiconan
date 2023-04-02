from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.build import can_run
import os

class WpiCommon:
    def generate_download_urls(self, library_name, version, os, arch, shared, debug):

        _os = {"Windows": "windows", "Linux": "linux", "Macos": "osx"}.get(os)
        _arch = arch.lower().replace("_", "-")
        _debug = debug.lower()

        if _os == "osx":
            _arch = "universal"

        if _os == "linux" and arch == "armv7":
            _arch = "athena"

        base_url = f"https://frcmaven.wpi.edu/artifactory/release/edu/wpi/first/{library_name}/{library_name}-cpp/{version}/{library_name}-cpp-{version}-"
        header_url = base_url + "headers.zip"

        static_str = "" if shared else "static"
        debug_str = "debug" if _debug == "debug" else ""

        lib_url = base_url + f"{_os}{_arch}{static_str}{debug_str}.zip"

        return (header_url, lib_url)
    
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

class WpiCommonPkg(ConanFile):
    name = "wpicommon"
    version = "0.1"
    package_type = "python-require"