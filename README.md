# BODEX baseline: Springgrasp

### BODex: [Project page](https://pku-epic.github.io/BODex/) ｜ [Paper](https://arxiv.org/abs/2412.16490)

### Springgrasp: [Website](https://stanford-tml.github.io/SpringGrasp) [Paper](https://arxiv.org/abs/2404.13532)

## Environment
Follow the instructions in the README_official.md file to install the required packages.

## Generate the dataset

1. Link the dataset to the assets folder
ln -s ${YOUR_DATA_PATH} assets/DGNObj
ln -s ${YOUR_SPLIT_PATH} assets/DGNObj_split

2. Generate the dataset
```
python optimize_pregrasp.py # generate grasps for single object
python multi_plan.py        # generate grasps for multiple objects
```