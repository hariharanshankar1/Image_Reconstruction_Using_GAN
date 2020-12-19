import os
os.sys.path.append('..')

from options import Options
from train_test_module import Trainer

opt = Options().parse()
trainer = Trainer(opt)
trainer.train()
trainer.test()
