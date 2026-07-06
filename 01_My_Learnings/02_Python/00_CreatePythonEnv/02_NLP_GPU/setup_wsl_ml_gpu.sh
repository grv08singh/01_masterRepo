#!/usr/bin/env bash
set -euo pipefail

# =========================
# 1) Verify GPU visibility
# =========================
nvidia-smi || { echo "GPU not visible in WSL. Install NVIDIA WSL driver on Windows first."; exit 1; }

# =========================
# 2) System prerequisites
# =========================
sudo apt update
sudo apt install -y wget curl bzip2 ca-certificates git build-essential

# =========================
# 3) Install Miniforge (RAPIDS-recommended)
# =========================
cd ~
if [ ! -d "$HOME/miniforge3" ]; then
  curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
  bash "Miniforge3-$(uname)-$(uname -m).sh" -b -p "$HOME/miniforge3"
  rm -f Miniforge3-*.sh
fi

eval "$($HOME/miniforge3/bin/conda shell.bash hook)"
conda init bash >/dev/null 2>&1 || true

# =========================
# 4) Conda channel config (RAPIDS requires conda-forge, not defaults)
# =========================
conda config --set channel_priority flexible
conda update -n base -y conda

# =========================
# 5) Create GPU environment
# =========================
ENV_NAME=gpu_rapids
PYTHON_VERSION=3.11
CUDA_VER=12.5

conda create -y -n "$ENV_NAME" -c rapidsai -c conda-forge -c nvidia \
  python="$PYTHON_VERSION" \
  cuda-version="$CUDA_VER" \
  rapids=25.06 \
  cudf cuml cugraph cuxfilter cupy dask-cuda \
  numpy pandas matplotlib seaborn plotly scikit-learn scipy statsmodels \
  tqdm nltk spacy emoji gensim textblob mlxtend \
  xgboost optuna catboost streamlit kaggle

conda activate "$ENV_NAME"

# =========================
# 6) PyTorch with CUDA 12.x (GPU build)
# =========================
conda install -y pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia

# =========================
# 7) TensorFlow with GPU support (CUDA 12 wheels via pip)
# =========================
pip install "tensorflow[and-cuda]"

# =========================
# 8) NLP / text utilities and extras
# =========================
pip install -U \
  contractions \
  fuzzywuzzy \
  python-levenshtein \
  langchain \
  langgraph \
  imbalanced-learn

# =========================
# 9) NLTK / spaCy model setup
# =========================
python -m nltk.downloader punkt stopwords wordnet omw-1.4 vader_lexicon
python -m spacy download en_core_web_sm || true

# =========================
# 10) Verify GPU-enabled libraries
# =========================
python - <<'PY'
import torch, tensorflow as tf
import cudf, cuml, cupy

print("PyTorch CUDA available:", torch.cuda.is_available())
print("PyTorch device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "None")

print("TensorFlow GPUs:", tf.config.list_physical_devices('GPU'))

print("cuDF version:", cudf.__version__)
print("cuML version:", cuml.__version__)
print("CuPy device:", cupy.cuda.runtime.getDeviceProperties(0)['name'])
PY

echo
echo "Done. Activate later with:"
echo "  eval \"\$(~/miniforge3/bin/conda shell.bash hook)\""
echo "  conda activate $ENV_NAME"