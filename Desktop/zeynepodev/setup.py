from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='shortestpath2220674052',  # Öğrenci numaranızı buraya ekleyin
    version='0.1.1',  # Sürüm numarasını artırdık
    author='Zeynep Oğulcan',  # Adınızı buraya yazın
    author_email='zeynepogulcan@hacettepe.edu.tr',  # E-posta adresinizi buraya yazın
    description='En kısa yolu bulan bir Python paketi',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zeyzey28/shortestpath',  # GitHub repo URL'nizi buraya yazın
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
) 