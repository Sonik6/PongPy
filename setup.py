import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pong", # Replace with your own username
    version="0.0.1",
    author="Slawek Galka",
    author_email="galka.slawek6@gmail.com",
    description="pong created from www.101computing.net",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sonik6/PongPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)