from setuptools import setup


setup(
    name='ipy',
    packages='ipy'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_limiter',
    ],
)
