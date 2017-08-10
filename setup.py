from pathlib import Path
from setuptools import setup


root = Path(__file__).parent.absolute()

with open(str(root / 'README.rst')) as f:
    long_description = f.read()


setup(
    name='obs-ws-rc',

    version='2.3.0',

    description=("asyncio-based Python 3.5+ client to obs-websocket "
                 "plugin for OBS Studio"),

    long_description=long_description,

    url="https://github.com/KirillMysnik/obs-ws-rc",

    author="Kirill Mysnik",

    author_email = "kirill@mysnik.com",

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Video',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='obs obs-websocket',

    packages=['obswsrc', ],

    install_requires=['websockets', ],

    python_requires='>=3.5',

    package_data={
        'obswsrc': ["protocol.json", ],
    }
)
