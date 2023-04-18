from conan import ConanFile
from conan.tools.files import get


class ctreRecipe(ConanFile):
    name = "ctre"
    version = "5.30.4"
    pro_version = "23.0.12"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"

    def build(self):
        tools_header_url, tools_lib_url = super().generate_ctre_url(
            "tools",
            self.pro_version,
            str(self.settings.os),
            str(self.settings.arch),
            str(self.settings.build_type),
            False
        )
        get(self, tools_header_url)
        get(self, tools_lib_url)
        
        api_cpp_header_url, api_cpp_lib_url = super().generate_ctre_url(
            "api-cpp",
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            str(self.settings.build_type),
            False
        )
        get(self, api_cpp_header_url)
        get(self, api_cpp_lib_url)

        cci_header_url, cci_lib_url = super().generate_ctre_url(
            "cci",
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            str(self.settings.build_type),
            False
        )
        get(self, cci_header_url)
        get(self, cci_lib_url)

        if self.options.target is None:
            simapicpp_header_url, simapicpp_lib_url = super().generate_ctre_url(
                "api-cpp-sim",
                self.version,
                str(self.settings.os),
                str(self.settings.arch),
                str(self.settings.build_type),
                True
            )
            get(self, simapicpp_header_url)
            get(self, simapicpp_lib_url)

            ccisim_header_url, ccisimcpp_lib_url = super().generate_ctre_url(
                "cci-sim",
                self.version,
                str(self.settings.os),
                str(self.settings.arch),
                str(self.settings.build_type),
                True
            )
            get(self, ccisim_header_url)
            get(self, ccisimcpp_lib_url)

            wpiapisim_header_url, wpiapisim_lib_url = super().generate_ctre_url(
                "wpiapi-cpp-sim",
                self.version,
                str(self.settings.os),
                str(self.settings.arch),
                str(self.settings.build_type),
                True
            )
            get(self, wpiapisim_header_url)
            get(self, wpiapisim_lib_url)

        wpiapi_header_url, wpiapi_lib_url = super().generate_ctre_url(
            "wpiapi-cpp",
            self.version,
            str(self.settings.os),
            str(self.settings.arch),
            str(self.settings.build_type),
            False
        )
        get(self, wpiapi_header_url)
        get(self, wpiapi_lib_url)
