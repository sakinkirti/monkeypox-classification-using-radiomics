from ImageSegmenter import ImageSegmenter as IS
from matplotlib import pyplot as plt

def main():

    img_path = '/Users/sakinkirti/Programming/Python/monkeypox-classification-using-radiomics/data/Monkey Pox/M01_01.jpg'
    result = IS.generate_mask(img_path=img_path)

    plt.matshow(result)

if __name__ == '__main__':
    main()