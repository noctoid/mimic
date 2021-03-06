from setuptools import setup, find_packages

setup(
    name='mimic',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='GNU GPL v3',
    author='yoko',
    author_email='i@noctoid.com',
    description='Mimimimimimimic!',
    install_requires=[
        'anyio==3.6.1', 'asgiref==3.5.2', 'certifi==2022.5.18.1', 'click==8.1.3', 'h11==0.12.0', 'h2==4.1.0',
        'hpack==4.0.0', 'httpcore==0.15.0', 'httpx==0.23.0', 'hyperframe==6.0.1', 'idna==3.3', 'rfc3986==1.5.0',
        'sniffio==1.2.0', 'starlette==0.20.0', 'uvicorn==0.17.6']
)
