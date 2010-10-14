from setuptools import setup, find_packages

setup(
    name='django-maroc-telecommerce',
    version='1.0.0',
    description='Django maroc telecommerce payment gateway.',
    author='Gregory Tappero',
    author_email='coulix@gmail.com',
        url='http://github.com/coulix/django-maroc-telecommerce',
    keywords = "django maroc",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='MIT License',
    platforms = ['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
