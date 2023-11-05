from setuptools import setup

setup(
    name = "dalle2-laion",
    version = "0.0.1",
    packages = ["dalle2-laion"],
    install_requires = [
        "packaging>=21.0",
        "pydantic>=1.9.0",
        "torch>=1.10",
        "pillow>=9.0.0",
        "numpy>=1.20.0",
        "click>=8.0.0"
        "dalle2-pytorch"
    ]
)
