from setuptools import setup, find_packages

def get_version():
    with open("src/{{cookiecutter.project_name}}/__version__.py") as f:
        version='temp-version' # keep pep8 happy
        exec(f.read()) # version defined here
        return version
    

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
