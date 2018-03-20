# Final Project Proposal
## Julia Zeh

### 3/21/18



#### Problem: 

Using an acoustic detector to find minke whale vocalizations. How many minke whales are vocalizing in a given area at a given time? How many minke whale vocalizations are there in a given passive acoustic recording?

#### Data: 

Example dataset with minke whale boings and trains. This package is trained for my specific dataset (passive acoustic data from New York in 2008 and 2009), but can operate on any acoustic recording file.

#### Tools: 

Pandas, Scikit learn, Scipy, Numpy, PyAudioAnalysis (1)

#### Novelty: 

Although various researchers have used automated detection algorithms to look at minke whale calls in passive acoustic recordings (2, 3), none of these are publicly available. This will be the first complete package for analyzing minke whale calls from passive acoustic recordings which is open access online.

#### Goal: 

Python library for use detecting minke whale vocalizations from any sound file. Tutorial in jupyter notebook for use on the example data. Dataframe with results of minke whale vocalizations detected by the algorithm for my New York dataset.


##### References
1. T. Giannakopoulos, pyAudioAnalysis: An Open-Source Python Library for Audio Signal Analysis. PLoS One. 10, e0144610 (2015).
2. D. Risch et al., Seasonal migrations of North Atlantic minke whales: novel insights from large-scale passive acoustic monitoring networks. Mov. Ecol. 2, 24 (2014).
3. M. Popescu et al., Bioacoustical Periodic Pulse Train Signal Detection and Classification using Spectrogram Intensity Binarization and Energy Projection (2013).
