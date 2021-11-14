from setuptools import setup

setup(name='lolpython',
      version='2.2.0',
      description='lolcat port of the ruby version',
      url='https://github.com/Abhishek8394/lol-cat-py',
      author='Abhishek8394',
      author_email='apbytes@gmail.com',
      license='GPLv3',
      packages=['lolpython'],
      entry_points={
            'console_scripts': ['lolpython=lolpython.main:main']
      },
      include_package_date=True,
      zip_safe=False)