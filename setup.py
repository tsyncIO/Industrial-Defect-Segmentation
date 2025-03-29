from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="steel-defect-detection",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Deep learning system for steel defect detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/steel-defect-detection",
    packages=find_packages(where=".", exclude=["tests*", "docs*", "notebooks*"]),
    package_dir={"": "."},
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.10.0",
        "torchvision>=0.11.0",
        "albumentations>=1.0.0",
        "numpy>=1.20.0",
        "opencv-python>=4.5.0",
        "pandas>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "flake8>=4.0",
        ],
        "api": [
            "fastapi>=0.70.0",
            "uvicorn>=0.15.0",
            "python-multipart>=0.0.5",
        ],
        "demo": [
            "gradio>=3.0",
            "streamlit>=1.0",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Manufacturing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        "console_scripts": [
            "steel-defect-train=steel_defect.training.cli:main",
            "steel-defect-api=steel_defect.api.cli:main",
        ],
    },
)