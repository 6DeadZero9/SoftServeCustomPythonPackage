from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class SoftServeExampleCBinding(ConanFile):
    name = "SoftServeExampleCBinding"
    author = "Ivan Iziumov"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("openssl/[>=3.5.0]")

    def build_requirements(self):
        self.tool_requires("cmake/[>=3.30]")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
