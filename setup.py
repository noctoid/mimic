from setuptools import setup, find_packages

setup(
    name='Mimic',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='GNU GPL v3',
    author='yoko',
    author_email='i@noctoid.com',
    description='Mimimimimimimic!',
    install_requires='''anyio==3.6.1
asgiref==3.5.2
click==8.1.3
h11==0.13.0
h2==4.1.0
hpack==4.0.0
hypercorn==0.13.2
hyperframe==6.0.1
idna==3.3
priority==2.0.0
sniffio==1.2.0
starlette==0.20.0
toml==0.10.2
typing_extensions==4.2.0
uvicorn==0.17.6
websockets==10.3
wsproto==1.1.0'''.split("\n")
)
