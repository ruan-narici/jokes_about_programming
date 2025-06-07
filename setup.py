from setuptools import setup, find_packages
from pathlib import Path

# Leitura dos arquivos
this_directory = Path(__file__).parent
readme = (this_directory / "README.md").read_text(encoding="utf-8")
requirements = (this_directory / "requirements.txt").read_text().splitlines()

setup(
    name="jokes_programming",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "jokes_programming=package_asks.run:run",
        ]
    },
    author="Ruan Narici",
    author_email="seuemail@example.com",  # opcional, mas recomendado
    description="Piadas engraçadas sobre programação e dados.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ruan-narici/jokes_about_programming",  # troque se quiser
    project_urls={
        "Source": "https://github.com/ruan-narici/jokes_about_programming",
        "Bug Tracker": "https://github.com/ruan-narici/jokes_about_programming/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Games/Entertainment :: Humor",
    ],
    python_requires=">=3.7",
    keywords=["piadas", "programação", "humor", "dados", "developer jokes"],
)
