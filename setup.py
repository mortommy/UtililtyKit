from setuptools import setup, find_packages


setup(
    name="UtilityKit",
    version="0.0.1",
    description="A collection of usefully utilities",
    author="Tommaso Morello",
    author_email="nonicknamethankyou@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="postegres, postgresql, file, filesystem",
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=["psycopg2"],
    py_modules=["utilitykit"],
)
