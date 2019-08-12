from PIL import Image
import imagehash

# img = Image.open(r'watermelon.jpg')
# region = (123, 518, 882, 523)
# # 裁切图片
# cropImg = img.crop(region)
# # 保存裁切后的图片
# cropImg.save(r'water-crop.jpg')

# 瘋狂截圖 => 裁切 => hash比較 ... until hash比較>0.95... => 暫時停止截圖(break):代表進到你要的畫面了
# ，執行想做的事... : 去領 => time.sleep() => 關閉


highfreq_factor = 1
hash_size = 8
img_size = hash_size * highfreq_factor

hash1 = imagehash.phash(Image.open('button-ex.jpeg'), hash_size=hash_size, highfreq_factor=highfreq_factor)
print(hash1)
# > 354adab5054af0b7

hash2 = imagehash.phash(Image.open('test.jpeg'), hash_size=hash_size, highfreq_factor=highfreq_factor)
print(hash2)
# > 5b7724c8bb364551

print(1 - (hash1 - hash2)/len(hash1.hash)**2)  # 相似性
