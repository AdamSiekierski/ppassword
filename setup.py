from setuptools import setup

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
      'ppassword = ppassword.main:main'
    ]
  }
)