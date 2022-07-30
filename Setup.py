from setuptools import setup, find_packages
import codecs
import os




VERSION = '0.0.1'
DESCRIPTION = 'A basic fibonacci package'

# Setting up
setup(
    name="FibApo",
    version=VERSION,
    author="Abdurrahman Pülat",
    author_email="<abdurrahmanulat9@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)