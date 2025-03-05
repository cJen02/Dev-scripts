module load python/3.10
python3.10 -m venv ./.venv
ls -a

source .venv/bin/activate

# packages
pip install myosuite
pip install stable_baselines3
pip install tensorboard

deactivate
