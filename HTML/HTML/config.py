from pathlib import Path

data_dir = Path(__file__).parent / '../../data'

test_path = data_dir / 'test.csv'
train_path = data_dir / 'train.csv'
train_label_path = data_dir / 'train_label.csv'