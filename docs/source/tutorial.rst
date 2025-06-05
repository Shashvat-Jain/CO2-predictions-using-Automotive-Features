Tutorial
========

This tutorial walks you through installing the package, running the CLI tool,
and using the Python API for custom workflows.

Contents:

.. toctree::
   :maxdepth: 2

1. Installation
2. CLI Usage
3. Python API
4. Loading Your Own Model

---

Installation
------------

First, install from PyPI:

.. code-block:: bash

   pip install co2_emissions_ml

Or install the bleeding‐edge version from GitHub:

.. code-block:: bash

   pip install git+https://github.com/Shashvat-Jain/CO2-predictions-using-Automotive-Features.git

---

CLI Usage
---------

Once installed, the `run_co2` console script is available.

Predict on a new dataset **without** CO₂ targets:

.. code-block:: bash

   run_co2 --data path/to/new_data.csv \
           --model path/to/bundle.pkl \
           --output path/to/predictions.csv

Train and evaluate on data **with** CO₂ targets:

.. code-block:: bash

   run_co2 --data path/to/labeled_data.csv \
           --target "CO2 Emissions (g/km)" \
           --output path/to/results.csv

---

Python API
----------

You can also call everything programmatically:

.. code-block:: python

   import pandas as pd
   import joblib
   from co2_emissions_ml.pipeline import run_pipeline
   from co2_emissions_ml.models import predict_bundle

   # 1) Train & evaluate
   bundle, metrics = run_pipeline(
       data_path="data/labeled_data.csv",
       target_col="CO2 Emissions (g/km)"
   )
   print(metrics)

   # 2) Inference only
   df_new = pd.read_csv("data/new_data.csv")
   predictions = predict_bundle(bundle, df_new)
   df_new["predicted_co2"] = predictions
   df_new.to_csv("data/predicted.csv", index=False)

---

Loading Your Own Model
----------------------

If you have a serialized bundle saved as `bundle.pkl`:

.. code-block:: python

   import joblib
   from co2_emissions_ml.models import predict_bundle
   import pandas as pd

   bundle = joblib.load("models/bundle.pkl")
   df = pd.read_csv("path/to/new_vehicles.csv")
   df["predicted_co2"] = predict_bundle(bundle, df)
   df.to_csv("predictions.csv", index=False)
