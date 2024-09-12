from setuptools import find_packages, setup

setup(
    name='custom_bot',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'discord.py',
        'pip',
        'pyyaml',
    ],
    author='Your Name',
    author_email='your_email@example.com',
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-github/MCC',  # Your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Your license if applicable
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'mcc=bot.main:run',
        ],
    },
    zip_safe=False,
)
