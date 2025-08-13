from setuptools import find_packages, setup

setup(
    name="dagster-analytics",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dagster-snowflake",
        "dbt-snowflake",
        "boto3",
        "pandas",
        "pyarrow",
        "simple-salesforce",
    ],
)
