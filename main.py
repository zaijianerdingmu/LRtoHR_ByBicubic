import os
import argparse
import cv2
 
# parse args
parser = argparse.ArgumentParser(description='Upsize images using bicubic interpolation')   #参数说明，用bicubic法对图片进行放大
##############################需要修改的部分#############################
parser.add_argument('--lr_img_dir', type=str, default=r'C:\Users\17865\Desktop\upsample\X2',    
                    help='path to low resolution image dir') #待上采样图片文件夹
parser.add_argument('--hr_img_dir', type=str, default=r'C:\Users\17865\Desktop\upsample\bicubic',
                    help='path to desired output path for Upsampled images') #结果保存路径，会自动生成存储结果的文件夹，如  X2result
parser.add_argument('--scale', type=int, default=2,
                    help='path to desired output dir for Upsampled images')#上采样倍率
##########################################################
args = parser.parse_args()
 
lr_image_dir = args.lr_img_dir
hr_image_dir = args.hr_img_dir
 
print(args.hr_img_dir)
print(args.lr_img_dir)
 
# create LR image dirs
os.makedirs(hr_image_dir + f"\X{args.scale}result", exist_ok=True) #创建保存结果的文件夹
 
 
supported_img_formats = (".bmp", ".dib", ".jpeg", ".jpg", ".jpe", ".jp2",
                         ".png", ".pbm", ".pgm", ".ppm", ".sr", ".ras", ".tif",
                         ".tiff")
 
# Upsample LR images
for filename in os.listdir(lr_image_dir):    #遍历低分图片文件夹中的每一个低分图片
    if not filename.endswith(supported_img_formats):   #如果当前遍历的文件的后缀不是能够上采样的文件
        continue                              #就跳过当前文件
 
    name, ext = os.path.splitext(filename)   #将文件名和其后缀分开
    # Read LR image
    lr_img = cv2.imread(os.path.join(lr_image_dir, filename))    #用完整的全路径读取当前图片
 
 
    # Upsample image
    hr_image = cv2.resize(lr_img, (0, 0), fx=int(f"{args.scale}"), fy=int(f"{args.scale}"), interpolation=cv2.INTER_CUBIC)    #
    cv2.imwrite(os.path.join(hr_image_dir + f"\X{args.scale}result", f"x{args.scale}_"+filename.split('.')[0]  + ext), hr_image) #保存高分辨率图像

print("上采样完成")