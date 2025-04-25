from setuptools import setup, find_packages

setup(
    name="dns_analyzer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'dnspython>=2.0',
        'tqdm>=4.0',
        'Jinja2>=3.0'
    ],
    entry_points={
        'console_scripts': [
            'dnsanalyze = dns_analyzer.cli:main'
        ]
    },
    package_data={
        'dns_analyzer': ['templates/*.html']
    },
    include_package_data=True,
)
