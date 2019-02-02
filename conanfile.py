from conans import ConanFile, CMake

class ProtobufQt(ConanFile):
    name = "protobuf-qt"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = "protobuf/3.6.1@bincrafters/stable"
    exports_sources = "*"
    generators = "cmake"

    def configure(self):
        pass
        self.options["protobuf"].shared = True

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()

        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        pass
