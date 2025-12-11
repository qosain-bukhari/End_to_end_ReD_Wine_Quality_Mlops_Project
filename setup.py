import setuptools

long_description = "End-to-end Red Wine Quality MLOps Project"
__version__ = "0.0.1"

REPO_NAME = "End_to_end_ReD_Wine_Quality_Mlops_Project"
AUTHOR = "qosain-bukhari"
EMAIL = "bukhariqosain824@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=EMAIL,
    description="A complete end-to-end MLOps project for predicting wine quality using Red Wine dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",

    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)