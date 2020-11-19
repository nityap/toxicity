# toxicity
## Setup
```
conda env -n toxicity python=3.8
conda activate toxicity
pip install -r requirements.txt
```

## Running triggers code
```
cd universal_triggers
export PYTHONPATH=.

# creating triggers
python gpt2/create_adv_token.py

# sampling with triggers
python gpt2/sample_from_gpt2.py
```
