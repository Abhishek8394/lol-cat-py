from setuptools import setup

setup(name='lolpy',
      version='0.1',
      description='lolcat port of the ruby version',
      url='https://github.com/Abhishek8394/lol-cat-py',
      author='Abhishek8394',
      author_email='apbytes@gmail.com',
      license='GPLv2',
      packages=['lol_py'],
      entry_points={
            'console_scripts': ['lolpy=lol_py.main:main']
      },
      include_package_date=True,
      zip_safe=False)