import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    
setuptools.setup(
     name = 'PyImpetus',  
     version = '1.0.0',
     author = "Atif Hassan",
     author_email = "atif.hit.hassan@gmail.com",
     description = "PyImpetus is a feature selection algorithm which considers features both separately and together as a group in order to provide not just the best set of features but also the best combination of features",
     long_description = long_description,
     long_description_content_type = "text/markdown",
     url = "https://github.com/atif-hassan/PyImpetus",
     py_modules = ["PyImpetus"],
     package_dir = {'': 'src'},
     install_requires = ["pandas", "scikit-learn", "numpy"],
     include_package_data = True,
     classifiers = [
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         #"License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ]
 )
