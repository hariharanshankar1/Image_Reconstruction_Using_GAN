Prerequisites to Project: 

Most of the prerequistes will be preinstall in google colab. Usage of cuda helps in reducing execution time.  

	Google Colab Account
	Python 3.7
	NVIDIA GPU + CUDA CuDNN (CUDA 10.0)
	Pytorch 1.2.0
	TensorboardX

Source Code sturture:
 
	model/ --contains generative and discriminative models files
		generator.py
		discriminator.py
		vgg_init.py
	dataset.py --Python file to load the dataset.
	loss.py --Python file to calculate loss functions.
	options.py --Python file to parse the arguments.
	invoke_train_test.py --Python file which used to call train and test functions.
	train_test_module.py --Python file where training and testing happens.
	plotgraph.py - Python file to plot the graph for epochs vs PSNR, SSIM and error.


Steps to Run the code:
we used google colab as cuda and most of the libraries is pre-installed for use.

	1. Load the data set and source code into your google drive and mount your it into your notebook 			with GPU runtime.
	2. Next, run  this command in a code cell.
		!python invoke_train_test.py with dersired arguments 
			--train_dataset -path to training dataset
    			--dev_dataset -path to development dataset
			--test_dataset -path to testing dataset
			--lr -learning rate
			--batch_size -batch size
			--iterator_number -number of iterator
			--checkpoint_path -path to checkpoint
			--load -whether to load the last model
			--save -path to save results
	3. Code will run.

Once all the values of PSNR, SSIM and error is computed for various epochs, those values are fed into the plotgraph.py file and the graph is plot.
