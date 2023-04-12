from conan import ConanFile


class wpiutilRecipe(ConanFile):
    name = "wpiutil"
    version = "2023.4.3"
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.WpiCommon"
