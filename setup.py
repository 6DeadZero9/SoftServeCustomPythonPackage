from setuptools import setup, find_packages

setup(
    name="soft_serve_custom_python_package",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "soft_serve_custom_python_package": ["libSoftServeExampleCBinding.so"],
    },
    include_package_data=True,
    author="Ivan Iziumov",
    author_email="iv.izyumov@gmail.com",
    description="Basic Python binding for C",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/6DeadZero9/SoftServeCustomPythonPackage",
)
