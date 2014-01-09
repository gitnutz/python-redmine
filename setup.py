from setuptools import setup, find_packages


setup(
    name='python-redmine',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/maxtepkeev/python-redmine',
    license=open('LICENSE').read(),
    author='Max Tepkeev',
    author_email='tepkeev@gmail.com',
    description='Library for communicating with a Redmine project management application',
    long_description=open('README.rst').read(),
    keywords='redmine',
    install_requires=['requests >= 2.1.0'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)