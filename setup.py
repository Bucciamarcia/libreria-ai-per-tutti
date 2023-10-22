from setuptools import setup

setup(
    name='libreria_ai_per_tutti',
    version='0.1.3',
    py_modules=['libreria_ai_per_tutti'],
    install_requires=[
        "openai",
        "weaviate-client",
        "tiktoken",
        "langchain",
    ]
)