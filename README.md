# Deep-Oscillometry
This repository contains the code of pre processing and deep learning model that was employed in our work: A Hybrid Deep Morpho-Temporal Framework for Oscillometric Blood Pressure Measurement

#Running the code
1 - The datasets subdirectories should be created as follows:
	root directory/OMW1
	root directory/CP_LPf
	root directory/indf
	root directory/denoise

2 - Run the Matlab code, which is included in the dataset folder, to prepare to generate files.
	
3 - Using the 'DeepOscillometry.yml' file and Anaconda, install all the required packages:
	conda env create -f DeepOscillometryEnv.yml
	
4 - The environment should be activated.

5 - Open the 'Pre Processing.py' file and run the preprocess function first, then the single_interpolation function.

6 - Save the preprocessed fie in defined direction.

7 - Run "Model.py" to train the network.

8 - Run "Test.py".
