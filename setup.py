from setuptools import setup, find_packages

setup(
    name='gisd',
    version='1.0.0',
    url='https://github.com/yooha1003/gisd',
    author='Uksu, Choi',
    author_email='qtwing@naver.com',
    description='Google image searching and downloading script',
    packages=find_packages(),
    install_requires=['selenium', 'argparse', 'tqdm', 'time', 'requests', 'urllib'],
)
