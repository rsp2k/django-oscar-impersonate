from setuptools import setup, find_packages

from oscar_impersonate import get_version


setup(
    name='django-oscar-pistachio',
    version=get_version(),
    url='https://github.com/rsp2k/django-oscar-impersonate',
    author="Ryan Malloy",
    author_email="ryan@supported.systems",
    description="🥸 Wrapper of django-impersonate for django-oscar. Fork of django-oscar-impersonate, which was abandoned. Named after Dana Carvey's character in 'The Master of Disguise (2003)'. Am I not turtley enough for the turtle club? 🐢 ",
    long_description=open('README.rst').read(),
    keywords="django, oscar, impersonate",
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-impersonate>=0.8.1',
        'django-oscar>=0.7',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
