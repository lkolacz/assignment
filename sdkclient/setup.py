from setuptools import setup, find_packages


def readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()


setup(
    name='sdkclient',
    version='0.0.1',
    description='This is a SDK client to communicate with webapp.',
    long_description=readme(),
    keywords='qredo webapp sdk client sum calculation',
    url='https://github.com/qredo-external/lkolacz.git',
    project_urls={
        "Bug Tracker": "https://github.com/qredo-external/lkolacz/issues",
    },
    author='Leszek Andrzej Kołacz',
    author_email='lkolacz@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "setuptools",
        "wheel",
        "flake8",
        "requests"
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)