#!/usr/bin/env python3

# +------------------------+			   
# | Created with Sailboat  |			   
# |			                   |			   
# | Do not edit this file  |			   
# | directly. Instead  	   |			   
# | you should edit the	   |			   
# | `sailboat.toml` file.  |			   
# +------------------------+	

import setuptools

try:
  with open("README.md", "r") as fh:
	  long_description = fh.read()
except:
	long_description = "# Test_Project\n\n### Contributors\n- Cole Wilson\n### Contact\n<> "

options = {
	"name":"sail-test",
	"version":"1.0.0",
	"scripts":['bin/ctest'],
	"entry_points":{
		'console_scripts': [],
	},
	"author":"Cole Wilson",
	"author_email":"",
	"description":"",
	"long_description":long_description,
	"long_description_content_type":"text/markdown",
	"url":"https://github.com/cole-wilson/sail-test",
	"packages":setuptools.find_packages(),
	"install_requires":[],
	"classifiers":["Programming Language :: Python :: 3"],
	"python_requires":'>=3.6',
	"package_data":{"": [],},
	"license":"MIT",
	"keywords":'',
}

custom_options = {}

if __name__=="__main__":
	setuptools.setup(**custom_options,**options)