# Final Project Proposal
## Julia Zeh

### 3/21/18



#### Problem: 

I propose to develop a Python library which detects minke whale vocalizations and summarizes the results. I will train an existing audio analysis tool (1) using known recordings of minke whales (2). This library will be useful in passive acoustic analyses, particularly for research in North Atlantic regions like New York, where minke whales are poorly studied. This library will answer questions like how many minke whales are vocalizing in a given area at a given time and how many minke whale vocalizations are there in a given passive acoustic recording?

#### Data: 

I will provide an example dataset (2) with minke whale boings which can be used to test the package and will be uploaded along with the documentation and scripts. This package will be trained for my own specific dataset (passive acoustic data obtained from the Wildlife Conservation Society, WCS), but will be able to operate on any acoustic recording file.

#### Tools: 

The main tool I will be using for this project is pyAudioAnalysis, a well-documented open-source code for analysis of audio files in Python (1). pyAudioAnalysis has very thorough documentation and a function for training classifiers of audio segments, which is why I have chosen to use it. I will also be using the Scikit learn package as scripted in PyAudioAnalysis in order to train the software to detect minke whale calls. I will organize my results in a Pandas DataFrame.

#### Novelty: 

Although various researchers have used automated detection algorithms to look at minke whale calls in passive acoustic recordings (3, 4), none of these are publicly available. Thus, there is very little public information to base a project like this off of and this will be the first publicly available tool for minke whale acoustic detection. Additionally, training an audio analysis library for cetacean research is a novel idea. I have found no documentation of use of pyAudioAnalysis for bioacoustic research. 

#### Goal: 

By the deadline, I will have a Python library for use detecting minke whale vocalizations from any sound file written using the pyAudioAnalysis package. I will also have a tutorial in jupyter notebook for use on the example data and a dataframe with the final results of minke whale vocalizations detected by the algorithm for my WCS dataset. With more time and effort, I may also look into reviewing false detections produced by this method and specializing a detector for certain regions based on variations in animal vocalizations and background noise levels. 


##### References
1. T. Giannakopoulos, pyAudioAnalysis: An Open-Source Python Library for Audio Signal Analysis. PLoS One. 10, e0144610 (2015).
2. http://ocr.org/sounds/minke-whale/
3. D. Risch et al., Seasonal migrations of North Atlantic minke whales: novel insights from large-scale passive acoustic monitoring networks. Mov. Ecol. 2, 24 (2014).
4. M. Popescu et al., Bioacoustical Periodic Pulse Train Signal Detection and Classification using Spectrogram Intensity Binarization and Energy Projection (2013).
