from setuptools import setup

setup(
    name='libreria_ai_per_tutti',
    version='0.1',
    py_modules=['ai_script'],
    install_requires=[
        "openai",
        "weaviate-client"
    ]
)