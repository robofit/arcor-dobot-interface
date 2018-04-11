# ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['art_dobot_interface'],
    package_dir={'art_dobot_interface': 'src/art_dobot_interface'},
)

setup(**setup_args)
