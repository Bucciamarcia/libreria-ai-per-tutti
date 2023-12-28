from setuptools import setup

setup(
    name='libreria_ai_per_tutti',
    version='0.1.6',
    py_modules=['libreria_ai_per_tutti'],
    install_requires=[
        "openai>=1.2.0",
        "weaviate-client",
        "tiktoken",
        "langchain",
    ]
)