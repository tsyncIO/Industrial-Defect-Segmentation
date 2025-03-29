import pytest
from steel_defect.data import SteelDataset

def test_dataset_initialization():
    dataset = SteelDataset(df=None, data_folder="data")
    assert dataset is not None