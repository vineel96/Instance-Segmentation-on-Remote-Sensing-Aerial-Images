# Instance Segmentation on Remote Sensing Aerial Images

## Abstract
Detecting and segmenting objects in remote sensing aerial images is challenging due to presence of very small target objects existing at different scales with complex
backgrounds. We present architecture which address this problem. Firstly, We use efficientdet as backbone network which helps in multi-scale object detection (small and large objects) through feature fusion and helps in model scaling along resolution, depth, and width for all backbone, feature network. Second, to increase receptive field and allow dense feature extraction we use atrous convolutions. Third, we use protonet to produce higher quality  masks due to global context of semantic information which also learns to localize instances on its own via different activations in its prototypes. Finally we combine all these sub modules to form one network.

![Architecture](https://github.com/vineel96/Instance-Segmentation-on-Remote-Sensing-Aerial-Images/blob/master/diagrams/architectrure.png)

## Datasets
### VHR-10 Remote Sensing Dataset
Preprocessed VHR-10 datasets are available in this repository, under VHR10_dataset.
Link to Dataset: [VHR-10 Dataset](https://github.com/chaozhong2010/VHR-10_dataset_coco)

## Model training and evaluation
Training: python train.py --config=yolact_base_config <br/>
Evaluation: python eval.py --trained_model=weights/file_name.pth

## Ablation Studies
To develop an understanding of which model components influence performance, a comprehensive ablation study is performed
Different Configurations were considered which involves:
- Change in dilation rates of atrous convolutions
- Insertion of atrous convolutions at different parts of the encoder
- Change in dimension of input image
- Use of different EfficientNet backbones
For results and comparisions refer this presentation: [instance segmentation](https://docs.google.com/presentation/d/1dSUykPfLs8NqAJ7roL3_IhRMO0JwRK3a_Dq2ceYzB98/edit#slide=id.g121927a1189_0_545)

## Qualitative Results 

Ground Truth             |  Base Model(Yolact) |  Proposed Method Prediction
:-------------------------:|:-------------------------: |:-------------------------:
![](https://github.com/vineel96/Instance-Segmentation-on-Remote-Sensing-Aerial-Images/blob/master/diagrams/gt-1.png)  |  ![](https://github.com/vineel96/Instance-Segmentation-on-Remote-Sensing-Aerial-Images/blob/master/diagrams/yolact-1.png) |  ![](https://github.com/vineel96/Instance-Segmentation-on-Remote-Sensing-Aerial-Images/blob/master/diagrams/prop-1.png)
![](https://github.com/vineel96/Instance-Segmentation-on-Remote-Sensing-Aerial-Images/blob/master/diagrams/gt-2.png)  |  ![](https://github.com/vineel96/Instance-Segmentation-on-Remote-Sensing-Aerial-Images/blob/master/diagrams/yolact-2.png) |  ![](https://github.com/vineel96/Instance-Segmentation-on-Remote-Sensing-Aerial-Images/blob/master/diagrams/proposed-2.png)

## Acknowledgment
This repo uses base codes with modifications from the following methods:
[EfficientDet](https://github.com/xuannianz/EfficientDet),
[Yolact](https://github.com/dbolya/yolact)
