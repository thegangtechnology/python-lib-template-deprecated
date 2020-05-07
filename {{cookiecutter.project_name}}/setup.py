from setuptools import setup, find_packages
from os.path import join, dirname


def get_version():
    fname = join(dirname(__file__), "src/{{cookiecutter.project_name}}/__version__.py")
    with open(fname) as f:
        ldict={}
        code = f.read()
        exec(code, globals(), ldict) # version defined here
        return ldict['version']
    

setup(name='{{cookiecutter.project_name}}',
      version=get_version(),
      description='',
      long_description=open('README.md').read().strip(),
      author='',
      author_email='',
      url='',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      py_modules=['{{cookiecutter.project_name}}'],
      install_requires=[
          'numpy'
      ],
      extras_require={
          'dev': [
              'ipykernel',
              'mypy',
              'autopep8',
              'pytest',
              'pytest-cov'
          ],
          'test': [
              'pytest',
              'pytest-cov'
          ]
      },
      license='Private',
      zip_safe=False,
      keywords='',
      classifiers=[''])
