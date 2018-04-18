from imdb.training.Pickler import *
from imdb.training.Trainer import *

print("\nLoading...")
Pickler.run()

print("\nTraining...")
Trainer.run()