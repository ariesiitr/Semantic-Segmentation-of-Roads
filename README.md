# Semantic-Segmentation-of-Roads
Recruitment Project for 2nd Year
## Problem Statement

<p align=justify>While using GPS mapping services like Google Maps, one might observe that they are able to mark out where roads or travelable paths are located on the map. The proposed problem is similar: Given an image taken by satellite, segment out road pixels from those that aren’t roads (for e.g., pixels that include buildings, trees, water bodies etc). The aim shall be to classify individual pixels to generate a black-and-white binary mask for the original image, depicting roads with white pixels and everything else in black. This problem is known as <b>Semantic Segmentation</b> in the domain of Computer Vision.</p>

## Solution
We used __DeepLabV3+__ model to [segment out road pixels from non-road pixels](./code/model_training.ipynb).
### Dataset used: 
The dataset that we used to train and validate the model is [__Massachusetts Roads Dataset__](https://www.cs.toronto.edu/~vmnih/data/). 

<center><img src="./assets/sample_img_mask_pair.png" height="300"/></center>
<h4><center>Sample Image-Mask Pair</center></h4>

<p align=justify>Since the images were quite large (about 1500 pixels x 1500 pixels), to get better segmentation results, the dataset was <a href="./code/ML_dataset_processing.ipynb">preprocessed</a> before training. We cut the images to a smaller size (256 pixels x 256 pixels, segmented out the roads for these new smaller images and finally stitched back the output masks that we got.</p>

### Model used: 
The architecture of __DeepLabV3+__ looks like: 

<center><img src="https://miro.medium.com/max/1000/1*2mYfKnsX1IqCCSItxpXSGA.png" width="750"/></center>
<h4><center><a href="https://arxiv.org/abs/1802.02611">Image Source: DeepLabV3+ [Liang-Chieh Chen et al.]</a></center></h4>

## Results
The results produced were like:

<center><img src="./assets/sample_result_final.png" height="200"/></center>

## Summary
The overall process can be summarised as:

<center><img src="./assets/overall_process.png"/ width="750"></center>

## Mentor: 
- Shrashtika Singh

## Team Members:
- Apurba Prasad Padhy
- Ayushi Raj
- Tushar Sahu