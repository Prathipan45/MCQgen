from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='prathipan',
    author_email='prathipan539@gmail.com',
    install_requires=["langchain-google-genai","google-generativeai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)