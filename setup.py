from setuptools import setup, find_packages

setup(
    name="co2_emissions_ml",
    version="1.0.0",
    description="End-to-end ML pipeline for vehicle CO2 emissions prediction",
    author="Shashvat Jain",
    author_email="20je0897@mc.iitism.ac.in",
    url="https://github.com/Shashvat-Jain/CO2-predictions-using-Automotive-Features/",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        # mirror your requirements.txt here
    ],
    entry_points={"console_scripts": ["run_co2=src.pipeline:run_pipeline"]},
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
