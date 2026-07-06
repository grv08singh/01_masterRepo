#!/usr/bin/env bash
set -euo pipefail

# =========================
# 1) System prerequisites
# =========================
sudo apt update
sudo apt install -y wget curl bzip2 ca-certificates git build-essential

# =========================
# 2) Install Miniconda
# =========================
cd ~
MINICONDA_SH=Miniconda3-latest-Linux-x86_64.sh

if [ ! -f "$MINICONDA_SH" ]; then
  wget -O "$MINICONDA_SH" https://repo.anaconda.com/miniconda/$MINICONDA_SH
fi

bash "$MINICONDA_SH" -b -p "$HOME/miniconda3"
rm -f "$MINICONDA_SH"

# Initialize conda for current shell
eval "$($HOME/miniconda3/bin/conda shell.bash hook)"
conda init bash >/dev/null 2>&1 || true

# =========================
# 3) Configure conda
# =========================
conda config --set auto_activate_base false
conda config --add channels conda-forge
conda config --set channel_priority strict

# Update conda itself
conda update -n base -y conda

# =========================
# 4) Create CPU environment
# =========================
ENV_NAME=base_cpu
PYTHON_VERSION=3.11

conda create -y -n "$ENV_NAME" python="$PYTHON_VERSION" pip

conda activate "$ENV_NAME"

# =========================
# 5) Core scientific stack
# =========================
conda install -y \
  numpy pandas matplotlib seaborn plotly scikit-learn scipy statsmodels \
  tqdm nltk spacy emoji gensim textblob mlxtend \
  xgboost optuna catboost streamlit kaggle \
  -c conda-forge

# =========================
# 6) Deep learning stack (CPU)
# =========================
# TensorFlow CPU and PyTorch CPU via conda-forge
conda install -y tensorflow-cpu pytorch-cpu torchvision torchaudio cpuonly -c conda-forge

# =========================
# 7) NLP / text utilities and extras
# =========================
pip install -U \
  contractions \
  fuzzywuzzy \
  python-levenshtein \
  langchain \
  langgraph \
  imbalanced-learn

# =========================
# 8) NLTK / spaCy model setup
# =========================
python -m nltk.downloader punkt stopwords wordnet omw-1.4 vader_lexicon
python -m spacy download en_core_web_sm || true

# =========================
# 9) Verify imports
# =========================
python - <<'PY'
import numpy, pandas, matplotlib, seaborn, plotly, sklearn, scipy, statsmodels
import nltk, spacy, emoji, gensim, textblob, xgboost, optuna, catboost
import streamlit, kaggle, contractions, fuzzywuzzy, langchain, langgraph
import imblearn
import tensorflow as tf
import torch

print("All major packages imported successfully.")
print("TensorFlow:", tf.__version__)
print("PyTorch:", torch.__version__)
PY

echo
echo "Done."
echo "Activate later with:"
echo "  eval \"\$(~/miniconda3/bin/conda shell.bash hook)\""
echo "  conda activate $ENV_NAME"