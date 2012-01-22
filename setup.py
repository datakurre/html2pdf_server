import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'xhtml2pdf',
    'pyramid',
    'pyramid_zcml',
    'pyramid_debugtoolbar',
    'waitress',
    ]

setup(name='html2pdf_server',
      version='0.0',
      description='html2pdf_server',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="html2pdf_server",
      entry_points = """\
      [paste.app_factory]
      main = html2pdf_server:main
      """,
      )

