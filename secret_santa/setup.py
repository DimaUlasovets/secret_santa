import os

from setuptools import find_packages, setup

setup(
    name="TMS-secret-santa",
    version="1.0.0",
    description="Diploma projects",
    packages=find_packages(),
    setup_requires=["wheel"],
    install_requires=[
        "Django==4.0.4",
        "djangorestframework==3.13.1",
        "djangorestframework-simplejwt==5.2.0",
        "psycopg2-binary==2.9.3",
        "pytest==7.1.2",
        "pytest-django==4.5.2",
        "pytest-factoryboy==2.3.1",
        "Faker==13.12.0",
        "ipython==8.4.0",
        "pytest-dotenv==0.5.2",
        "django-redis==5.2.0",
        "celery==5.0",
        "black==22.3.0",
        "flake8==4.0.1",
        "pre-commit==2.18.1",
    ],
    include_package_data=True,
)
