from setuptools import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name="ppassword",
  version='0.0.1',
  description='The safest, most reliable password manager, made by programmers, for programmers',
  author='Adam Siekierski',
  author_email='adam.siekiera@outlook.com',
  license='MIT',
  packages=['ppassword'],
  package_dir={
    'ppassword': 'src'
  },
  entry_points = {
    'console_scripts': [
      'ppassword = ppassword.ppassword:main'
    ]
  },
  install_requires=requirements
)