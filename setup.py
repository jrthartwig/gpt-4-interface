from setuptools import setup, find_packages

setup(
    name='gpt-4-interface',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'azure-storage-blob',
        'azure-functions',
        'openai',
        'pandas',
        'numpy',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'gpt-4-interface=src.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A custom GPT-4 interface for business development',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/gpt-4-interface',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)