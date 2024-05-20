<h2>iNeuron_End_to_End_DL_Live: End to End Chicken Disease CNN Project</h2>

<h3>Workflows:</h3>

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

<h3>How to run?</h3>
<h4>Steps:</h4>
Clone the repository using the command: git clone https://github.com/Akshay-Paunikar/iNeuron_End_to_End_DL_Live.git

<b>Step 1: Create a conda environment after opening the repository</b>

 - conda create -n CDC python=3.9 -y

 - conda activate CDC

<b>Step 2: Install the requirements</b>

 - pip install -r requirements.txt
 - Finally run the following command: python app.py

Now, open up you local host and port

<b>DVC cmd</b>

 - dvc init
 - dvc repro
 - dvc dag
