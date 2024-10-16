This Repo is the building blocs for the first ever Fake news and sentiment analysis corpus in the algerian dialect, it contains all the codes from the data analysis to training and all.

# 1 - FASSILA Analysis

This Python script performs analysis on Arabic language text data, including counting Modern Standard Arabic (MSA) words, determining vocabulary size, and counting Latin characters.

## Setup

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:

```bash
pip install pandas
```

## Clone the repository
```bash
git clone https://github.com/your_username/arabic-language-analysis.git
cd arabic-language-analysis
```
## Replace the file paths in the script with the paths to your dataset files
```bash
path = "path/to/your/msa_dataset.csv"
path2 = "path/to/your/latin_dataset.csv"
```
## Finally run the code
```bash
python analyze_arabic.py
```

## Replace `"path/to/your/msa_dataset.csv"` and `"path/to/your/latin_dataset.csv"` with the actual file paths to your MSA and Latin datasets. Also, make sure to name your Python script accordingly (e.g., `analyze_arabic.py`).

## Citation
```bibtex
@article{abdedaiem2023fake,
  title={Fake News Detection in Low Resource Languages using SetFit Framework},
  author={Abdedaiem, Amin and Dahou, Abdelhalim Hafedh and Cheragui, Mohamed Amine},
  journal={Inteligencia Artificial},
  volume={26},
  number={72},
  pages={178--201},
  year={2023}
}
```
