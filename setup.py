import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spdx-poetry-demo-ifpratik",
    version="0.0.1",
    author="Pratik Karanje",
    author_email="lfpratik@linuxfoundation.org",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lfpratik/spdx-poetry-demo",
    project_urls={
        "Bug Tracker": "https://github.com/lfpratik/spdx-poetry-demo/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "spdx_poetry_demo"},
    packages=setuptools.find_packages(where="spdx_poetry_demo"),
    python_requires=">=3.6",
)