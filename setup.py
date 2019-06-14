import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='AutoMacDoc',
     version='0.3',
     entry_points={"console_scripts": ["automacdoc = automacdoc.main:main"]},
     author="Alexandre Kempf",
     author_email="alexandre.kempf@¢ri-paris.org",
     description="Automatic generation of documentation for python projects",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     install_requires=['mkdocs', 'mkdocs-material', 'pymdown-extensions'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
 # url="https://github.com/javatechy/dokr",
