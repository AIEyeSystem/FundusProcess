import fundus_prep as prep
import glob
import os
import cv2 as cv
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def process(image_list, save_path):
    
    for image_path in image_list:
        # dst_image = os.path.splitext(image_path.split('\\')[-1])[0]+'.png' ### windows
        dst_image = os.path.splitext(image_path.split('/')[-1])[0]+'.png'
        dst_path = os.path.join(save_path, dst_image)
        if os.path.exists(dst_path):
            print('continue...')
            continue
        try:
            img = prep.imread(image_path)
            r_img, borders, mask = prep.process_without_gb(img)
            r_img = cv.resize(r_img, (512, 512))
            prep.imwrite(dst_path, r_img)
            # mask = cv.resize(mask, (800, 800))
            # prep.imwrite(os.path.join('./original_mask', dst_image), mask)
            print('process')
        except:
            print(image_path)
            continue


if __name__ == "__main__":

    image_list = glob.glob(os.path.join('/home/zack/data/myopia/BJO/h_myopia', '*.jpg'))
    save_path = prep.fold_dir('/home/zack/data/myopia/BJOProcessed/h_myopia')

    process(image_list, save_path)

        





