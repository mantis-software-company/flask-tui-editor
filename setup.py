import setuptools

setuptools.setup(
    name="Flask-TUI-Editor",
    version="1.0.0",
    author="Furkan Kalkan",
    author_email="furkankalkan@mantis.com.tr",
    description="Toast UI Markdown Editor Integration for Flask-WTF.",
    url="https://github.com/mantis-software-company/flask-tui-editor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['Flask', 'WTForms'],
    packages=['flask_tui_editor'],
    include_package_data=True,
    zip_safe=False,
)
