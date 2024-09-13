from setuptools import find_packages, setup

setup(
    author='Your Name',
    author_email='Your Email',
    classifiers=[
        'Development Status :: 1 - Alpha'
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
    ],
    description='The MCC STEMgineering club Discord bot is a unique application of computer science.',
    entry_points={
        'console_scripts': [
            'custom_bot=bot.main:run',
        ],
    },
    include_package_data=True,
    install_requires=[
        'discord.py',
        'pip',
        'pyyaml',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    maintainer='Brandon Cobb',
    name='custom_bot',
    packages=find_packages(),
    python_requires='>=3.8',
    url='https://github.com/brandongrahamcobb/MCC', 
    version='1.0.0',
    zip_safe=False,
)
