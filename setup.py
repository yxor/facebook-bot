from distutils.core import setup


setup(
    name = 'facebook-handler',
    packages = ['facebook-handler'],
    version = '0.1',
    license = 'MIT',
    description = 'A python library made with selenium to control a facebook account \
                without the use of the offical API',
    author = 'Ahmed Tounsi',
    author_email = 'ahmeddottounsi@gmail.com',
    url = 'https://github.com/ahmed-tounsi',
    download_url = 'https://github.com/ahmed-tounsi/facebookHandler/archive/0.1.tar.gz',
    keywords = ['facebook', 'selenium', 'facebook-bot'],
    install_requires =[
        'selenium',
    ],
    classifiers =[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)