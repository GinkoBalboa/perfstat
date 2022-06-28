import sys
import os
import time
import setuptools
import subprocess
from platform import system

# You can't use `pip install .` as pip copies setup.py to a temporary
# directory, parent directory is no longer reachable (isolated build) .
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, CURRENT_DIR)

if __name__ == '__main__':
    
    # Supported commands:
    # From internet:
    #   pip install perfstat
    # Locally for testing (from perfstat/python-packate dir)
    #   pip install -e . --force-reinstall -v
    
    # Build dist
    # python setup.py bdist_wheel --plat-name manylinux2014_x86_64

    with open("../README.md", "r") as fh:
        long_description = fh.read()

    tagName = "0.0.2"

    setuptools.setup(
        name="perfstat",
        version=tagName,
        author="Ginko Balboa",
        author_email="ginkobalboa3@gmail.com",
        description="Capturing performance statistics",
        packages=setuptools.find_packages(include=['perfstat', 'perfstat.*']),
        include_package_data=True,
        install_requires=['pandas'],
        long_description=long_description,
        long_description_content_type="text/markdown",
        project_urls={"github": "https://github.com/GinkoBalboa/perfstat"},
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: POSIX :: Linux",
            "Topic :: Software Development",
        ],
        python_requires='>=3.7',
        zip_safe=False,
    )
