from conan import ConanFile


class wpimathTest(ConanFile):
    python_requires = "wpicommon/0.1"
    python_requires_extend = "wpicommon.testPackageBase"
