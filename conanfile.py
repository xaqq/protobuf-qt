from conans import ConanFile, CMake

class ProtobufQt(ConanFile):
    name = "protobuf-qt"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    build_requires = "protobuf/3.6.1@bincrafters/stable"
    exports_sources = "*"
    generators = "cmake"
    keep_imports = True

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
        # Make sure to also package protobuf libraries
        self.copy('*.so*', 'lib', 'lib')

    def package_info(self):
        pass

    def imports(self):
        # Import protobuf libraries. We will repackage them alongside
        # our compiler plugin
        self.copy('*.so*', 'lib', 'lib')
