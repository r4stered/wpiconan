import os
from conan import ConanFile
from conan.tools.files import get, copy, replace_in_file
from conan.errors import ConanInvalidConfiguration
from conan.tools.cmake import CMakeToolchain

class riotoolchainRecipe(ConanFile):
    name = "riotoolchain"
    version = "v2023-8"
    package_type = "application"
    options = {"target": [None, "ANY"]}
    default_options = {"target": None}
    # Binary configuration
    settings = "os", "build_type", "arch"

    temp_package_folder = None

    def validate(self):
        settings_target = getattr(self, 'settings_target', None)
        if settings_target is None:
            print("Running as host")
            # It is running in 'host', so Conan is compiling this package
            if not self.options.target:
                raise ConanInvalidConfiguration("A value for option 'target' has to be provided")
        else:
            print("Running as compiler")
            if self.options.target:
                raise ConanInvalidConfiguration("Value for the option 'target' will be computed from settings_target")
            print("self.settings_target.arch: " + str(self.settings_target.arch))
            self.options.target = self.settings_target.arch
            if not (str(self.options.target) == "armv8" or str(self.options.target) == "armv7hf" or str(self.options.target) == "armv6" or str(self.options.target) == "armv7"):
                raise ConanInvalidConfiguration("Target arch not supported: " + str(self.options.target))
        
    def download_toolchain(self):
        #TODO: delicate version name
        target_arch_str = ""
        version_str = "10.2.0"
        if(str(self.options.target) == "armv8"):
            target_arch_str = "arm64-bullseye-2023"
        if(str(self.options.target) == "armv7hf"):
            target_arch_str = "armhf-bullseye-2023"
        if(str(self.options.target) == "armv6"):
            target_arch_str = "armhf-raspi-bullseye-2023"
        if(str(self.options.target) == "armv7"):
            target_arch_str = "cortexa9_vfpv3-roborio-academic-2023"
            version_str = "12.1.0"

        build_os_str = ""
        ext_str = "tgz"
        if str(self.settings_build.os) == "Windows":
            build_os_str = "w64-mingw32"
            ext_str = "zip"
        if str(self.settings_build.os) == "Macos":
            build_os_str = "apple-darwin"
        if str(self.settings_build.os) == "Linux":
            build_os_str = "linux-gnu"
        
        get(self, f"https://github.com/wpilibsuite/opensdk/releases/download/{self.version}/{target_arch_str}-{self.settings_build.arch}-{build_os_str}-Toolchain-{version_str}.{ext_str}")

    def generate(self):        
        self.temp_package_folder = str(self.package_folder).replace(os.sep, '/')
        self.download_toolchain()

        ext_str = ""
        if str(self.settings_build.os) == "Windows":
            ext_str = ".exe"

        bin_folder = os.path.join(self.package_folder, "roborio-academic", "bin").replace(os.sep, '/')

        tc = CMakeToolchain(self)
        tc.variables["CMAKE_SYSTEM_NAME"] = "Linux"
        tc.variables["CMAKE_SYSTEM_VERSION"] = "1"
        tc.variables["CMAKE_SYSTEM_PROCESSOR"] = "arm"
        tc.variables["CMAKE_SYSROOT"] = os.path.join(self.package_folder, "roborio-academic", "arm-nilrt-linux-gnueabi", "sysroot").replace(os.sep, '/')
        tc.variables["CMAKE_C_FLAGS"] = "-Wno-psabi"
        tc.variables["CMAKE_CXX_FLAGS"] = "-Wno-psabi"
        tc.variables["CMAKE_Fortran_FLAGS"] = "-Wno-psabi"
        tc.variables["CMAKE_C_COMPILER"] = os.path.join(bin_folder, "arm-frc2023-linux-gnueabi-gcc" + ext_str).replace(os.sep, '/')
        tc.variables["CMAKE_CXX_COMPILER"] = os.path.join(bin_folder, "arm-frc2023-linux-gnueabi-g++" + ext_str).replace(os.sep, '/')
        tc.variables["CMAKE_Fortran_COMPILER"] = os.path.join(bin_folder, "arm-frc2023-linux-gnueabi-gfortran" + ext_str).replace(os.sep, '/')
        tc.variables["CMAKE_AR"] = os.path.join(bin_folder, "arm-frc2023-linux-gnueabi-ar" + ext_str).replace(os.sep, '/')
        tc.variables["CMAKE_AS"] = os.path.join(bin_folder, "arm-frc2023-linux-gnueabi-as" + ext_str).replace(os.sep, '/')
        tc.variables["CMAKE_NM"] = os.path.join(bin_folder, "arm-frc2023-linux-gnueabi-nm" + ext_str).replace(os.sep, '/')
        tc.variables["CMAKE_LINKER"] = os.path.join(bin_folder, "arm-frc2023-linux-gnueabi-ld" + ext_str).replace(os.sep, '/')
        tc.variables["CMAKE_FIND_ROOT_PATH_MODE_PROGRAM"] = "NEVER"
        tc.variables["CMAKE_FIND_ROOT_PATH_MODE_LIBRARY"] = "ONLY"
        tc.variables["CMAKE_FIND_ROOT_PATH_MODE_INCLUDE"] = "ONLY"
        tc.variables["CMAKE_FIND_ROOT_PATH_MODE_PACKAGE"] = "ONLY"
        tc.generate()

    def package(self):
        copy(self, "*", self.build_folder, self.package_folder)
    
    def package_info(self):
        if self.temp_package_folder is not None:
            with open(os.path.join(self.package_folder, "conan_toolchain.cmake")) as f:
                s = f.read()
                if self.temp_package_folder not in s:
                    print('"{self.temp_package_folder}" not found in conan_toolchain.cmake.'.format(**locals()))
                    return
            
            # Safely write the changed content, if found in the file
            with open(os.path.join(self.package_folder, "conan_toolchain.cmake"), 'w') as f:
                print('Changing "{self.temp_package_folder}" to "{self.package_folder}" in conan_toolchain.cmake'.format(**locals()))
                s = s.replace(self.temp_package_folder, str(self.package_folder).replace(os.sep, '/'))
                f.write(s)

        f = os.path.join(self.package_folder, "conan_toolchain.cmake")
        self.conf_info.define("tools.cmake.cmaketoolchain:user_toolchain", [f])