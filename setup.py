import setuptools 
with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()
__version__ ="0.0.0"
REPO_NAME="Text-Summarizer"
AUTHOR_USER_NAME="Aryan"
SRC_REPO="text-summarization"
AUTHOR_EMAIL="aryankankeria331@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smuggypusss/text-summarization",
    project_urls={
        "Bug Tracker": "https://github.com/smuggypusss/text-summarization/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
    