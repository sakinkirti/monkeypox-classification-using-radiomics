# monkeypox-classification-using-radiomics
Creation of a ML model using a radiomics approach to classify monkeypox lesions

Image data gathered from: <br>
Ali, S. N., Ahmed, M. T., Paul, J., Jahan, T., Sani, S. M. Sakeef, Noor, N., & Hasan, T. (2022). Monkeypox Skin Lesion Detection Using Deep Learning Models: A Preliminary Feasibility Study. arXiv preprint arXiv:2207.03342.

This paper uses a deep learning model to classify lesions on the skin as monkeypox or not monkeypox. Here, I take a different approach by gathering radiomic data from the images using pyradiomics to generate tabular features of the images. Then I feed these values into a classical ML model (TBD) to classify the images as monkeypox or no monkeypox. The groud truth of these values can be found at data/mp-class_metadata.csv

This approach could be useful because of the consistency with which features are outputted when compared to a Deep Learning model