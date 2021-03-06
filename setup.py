from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f]

discription = "qwgc is a quantum walk graph classifier \
               for classification for Graph data."
setup(
    name="qwgc",
    version="0.0.3",
    description="Graph classifier based on quantum walk",
    long_description=discription,
    url="https://Chibikuri.github.io/qwgc",
    author="Ryosuke Satoh",
    author_email="ryosuke.satoh.wk@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="quantum walk machine learning",
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5",
)
