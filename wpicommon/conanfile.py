from conan import ConanFile

class WpiCommon:
    def generate_download_urls(self, library_name, version, os, arch, shared, debug):

        _os = {"Windows": "windows", "Linux": "linux", "Macos": "osx"}.get(os)
        _arch = arch.lower().replace("_", "-")
        _debug = debug.lower()

        if _os == "osx":
            _arch = "universal"

        base_url = f"https://frcmaven.wpi.edu/artifactory/release/edu/wpi/first/{library_name}/{library_name}-cpp/{version}/{library_name}-cpp-{version}-"
        header_url = base_url + "headers.zip"

        static_str = "" if shared else "static"
        debug_str = "debug" if _debug == "debug" else ""

        lib_url = base_url + f"{_os}{_arch}{static_str}{debug_str}.zip"

        return (header_url, lib_url)

class WpiCommonPkg(ConanFile):
    name = "wpicommon"
    version = "0.1"
    package_type = "python-require"