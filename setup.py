import setuptools

with open("README.md","r", encoding="utf-8") as f :
    long_description = f.read()
    
    
__Version__ = "0.0.0"

REPO_NAME = "End_End_Ml_project_with_mlflow"
AUTHOR_USER_NAME = 'HarishKumarSedu'
SRC_REPO = "mlProjects"
AUTHOR_EMIAL = 'harishkumarsedu@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__Version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMIAL,
    description="a samll Python packeage for Ml",
    Long_description=long_description,
    Long_description_content = "text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)