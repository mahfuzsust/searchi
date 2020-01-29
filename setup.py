import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='searchi',
     version='0.2',
     scripts=['searchi'] ,
     author="Mahfuzur Rahman",
     author_email="mahfuz.sust001@gmail.com",
     description="Search package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/mahfuzsust/searchi",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )

