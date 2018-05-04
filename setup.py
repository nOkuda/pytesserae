from setuptools import setup, find_packages

setup(
    name='pytesserae',
    version='0.0.1',
    description='Tesserae v5 sandbox',
    url='https://github.com/nOkuda/pytesserae',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='Tesserae',
    python_requires='~=3.5',
    packages=find_packages(exclude=['examples', 'tests', 'scripts']),
    install_requires=[
        'regex',
    ],
    include_package_data=True,
)
