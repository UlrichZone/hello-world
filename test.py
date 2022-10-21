
# import sys
# import pandas as pd

# for root, dirnames, filenames in os.walk(filepath):
#     for filename in filenames:
#     	filelist.append(os.path.join(root,filename))
#         print(os.path.join(root,filename))
# import os
# filelist=[]

# for root,dirs,files in os.walk("/Users/likorn/Desktop/Trade2/"):

#         filelist.append(join_dir)
#         print(os.path.join(root, dir))
#     for file in files:
#         print(os.path.join(root, file))
#     for dir in dirs:
#         join_dir = os.path.join(root, dir)
#         print(join_dir)
        



import os
 
 
image_path = '/Users/likorn/Desktop/Trade2/'
# 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
# 输入文件夹路径、空文件列表[]
# 返回 文件列表Filelist,包含文件名（完整路径）
# def get_filelist(dir, Filelist):
#     newDir = dir
#     if os.path.isfile(dir):
#         Filelist.append(dir)
#         # # 若只是要返回文件文，使用这个
#         # Filelist.append(os.path.basename(dir))
#     elif os.path.isdir(dir):
#         for s in os.listdir(dir):
#             # 如果需要忽略某些文件夹，使用以下代码
#             #if s == "xxx":
#                 #continue
#             newDir=os.path.join(dir,s)
#             get_filelist(newDir, Filelist)

# get_filelist(image_path)

# # if __name__ =='__main__' :
# #     list = get_filelist('/Users/likorn/Desktop/Trade2/', [])
# #     print(len(list))
# #     for e in list:
# #         print(e)


import glob

filepath=r'/Users/likorn/Desktop/Trade2/'
csv_img = glob.glob(filepath+'\*.csv')
print(csv_img)
