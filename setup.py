from setuptools import setup, find_packages

with open('README.md', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='pixaiAPI',
    version='0.1.11',
    author='shidktbw',
    description='An unofficial API for pixai.art for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    url='https://github.com/shidktbw/pixaiAPI',
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
)