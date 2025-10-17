import setuptools

setuptools.setup(
    name="PSY46050_Python-Git-Intigration",
    version="0.1.0",
    author="A. W. Muhtaseb",
    author_email="muhtaseb@uchicago.edu",
    description="Dummy Package for Python",
    url="https://bitbucket.org/psych46050/workspace/overview/",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'numpy',
        'scipy',
    ],
)
