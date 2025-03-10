from setuptools import setup, find_packages

# --- Basic Setup ---
setup(
    name='src',  # Required: Your package's name (must be unique on PyPI)
    version='0.1.0',  # Required: Start with 0.1.0 or 0.0.1, follow semantic versioning
    description='A short description of my package',  # Optional: Short and sweet
    long_description=open('README.md').read(), # Optional: from a file, usually README.md
    long_description_content_type='text/markdown',  # Important if using markdown in long_description
    url='https://github.com/yourusername/my_package',  # Optional: Link to your project's code repository
    author='Your Name',  # Optional: Your name or organization name
    author_email='your.email@example.com',  # Optional: Your email address
    license='MIT',  # Optional: Choose a license (e.g., MIT, GPL, Apache)
    classifiers=[  # Optional: Classifiers help users find your package
        'Development Status :: 3 - Alpha',  # Or 4 - Beta, 5 - Production/Stable
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='your keywords here, comma, separated', # Optional: keywords to help users find your package
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required: Automatically find packages
    python_requires='>=3.7', # Optional: specify a minimum python version
    install_requires=[  # Optional: List of required packages (dependencies)
        # 'requests>=2.20',
        # 'numpy',
    ],
    extras_require={  # Optional: Extra dependencies (e.g., for testing)
        'dev': ['pytest', 'flake8'],
    },
    # --- Entry Points (Optional, for command-line scripts) ---
    # entry_points={
    #     'console_scripts': [
    #         'my_script = my_package.my_module:main_function',
    #     ],
    # },
    project_urls={  # Optional: Links to documentation, bug tracker, etc.
        'Bug Reports': 'https://github.com/yourusername/my_package/issues',
        'Source': 'https://github.com/yourusername/my_package',
    },
)
