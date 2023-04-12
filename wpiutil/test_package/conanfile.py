from conan import ConanFile


class wpiutilTest(ConanFile):
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.testPackageBase"
