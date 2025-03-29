import argparse
from steel_defect.training import Trainer
from steel_defect.data import SteelDataset
from steel_defect.models import UNet, BCEDiceLoss

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=10)
    args = parser.parse_args()
    
    # Initialize components
    model = UNet()
    criterion = BCEDiceLoss()
    optimizer = torch.optim.Adam(model.parameters())
    
    # Create dummy datasets (replace with real ones)
    train_dataset = SteelDataset(df=None, data_folder="data/train")
    val_dataset = SteelDataset(df=None, data_folder="data/val")
    
    trainer = Trainer(model, train_dataset, val_dataset, criterion, optimizer)
    trainer.fit(args.epochs)

if __name__ == "__main__":
    main()from steel_defect.api import create_app
