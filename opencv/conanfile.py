from conan import ConanFile
from conan.tools.files import get, rename, collect_libs
import glob
import os


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

    def make_file_name(self, name):
        version = ".4.6"
        fileExt = ""
        if self.options.shared:
            fileExt = ".so"
        else:
            fileExt = ".a"

        final_name = name + fileExt + version
        if self.settings.build_type == "Debug":
            final_name = final_name + ".debug"

        return os.path.join(self.package_folder, "lib", final_name)

    def package_info(self):
        lib_names = [
            "opencv_arcuo",
            "opencv_calib3d",
            "opencv_core",
            "opencv_features2d",
            "opencv_flann",
            "opencv_gapid",
            "opencv_highgui",
            "opencv_imgcodecs",
            "opencv_imgproc",
            "opencv_ml",
            "opencv_objdetect",
            "opencv_photo",
            "opencv_stiching",
            "opencv_video",
            "opencv_videoio"
        ]

        lib_names = [self.make_file_name(lib) for lib in lib_names]

        print(lib_names)
        print(str(self.settings.os))
        print(self.options.shared)

        if str(self.settings.os) == "Linux" and self.options.shared:
            print("Using custom list")
            self.cpp_info.libs = lib_names
        else:
            print("Using collect libs")
            self.cpp_info.libs = collect_libs(self)
