from setuptools import setup, find_packages

setup(
    name="dns_analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'dnspython>=2.0',
        'reportlab>=3.6',
        'Jinja2>=3.0',
        'python-dotenv>=0.19'
    ],
    entry_points={
        'console_scripts': [
            'dnsanalyze = dns_analyzer.main:main'
        ]
    },
    package_data={
        'dns_analyzer': ['templates/*.html']
    },
    include_package_data=True,
)
