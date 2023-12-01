#画像処理ライブラリ

from PIL import Image, ImageFilter, ImageDraw
from tkinter import filedialog
import numpy as np
from matplotlib import pylab as plt

def pil_main():
    path = get_file_path()
    path2 = get_file_path()
    img = Image.open(path)
    img.show()

    print(img.format, img.size, img.mode)

    #クロップ・リサイズ
    cropp_resize(img)

    #回転する
    rotate(img)

    #2極化
    binarization(img)

    #輪郭抽出
    contour_extraction(img)

    #ぼかし
    img_blur(img)

    img2 = Image.open(path2)
    paste_an_image(img, img2)

    drawing_shapes(img2)

## fileパス取得
def get_file_path():

    typ = [('image','*.jpg'),('image','*.png')] 
    dir = 'C:\\'
    path = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 

    print(path)
    return path

def cropp_resize(img):
    #クロップ・リサイズ
    # (20,20)の座標から(100,100)までの座標部分を切り出し（クロップ）
    cropped = img.crop((20, 20, 100, 100))
    cropped.show()

    ### リサイズ（リサイズ後のサイズを指定）
    resized = img.resize((100, 100))
    resized.show() 

def rotate(img):
    #回転する
    rotate = img.rotate(50)
    rotate.show()

#2極化
def binarization(img):
    # グレースケール化
    grayscaled = img.convert('L')
    # 画像を配列に変換する
    img_array = np.array(grayscaled, 'f')
    # グレースケールのうち、白(0)と黒(255)の中間である128を基準に白黒へ変換
    img_array = (img_array > 128) * 255
    # matplotlibを使用して表示
    plt.imshow(img_array)

#輪郭抽出
def contour_extraction(img):
    blured = img.filter(ImageFilter.BLUR)
    blured.show()

#ぼかし
def img_blur(img):
    #通常ぼかし
    img.filter(ImageFilter.BLUR).show()

    #ガウスぼかし
    img.filter(ImageFilter.GaussianBlur(3)).show()

    #ボックスぼかし
    img.filter(ImageFilter.BoxBlur(3)).show()

#画像の貼り付け
def paste_an_image(img, img2):
    img.paste(img2.resize((100,100)), (25, 25))

    img.show()

#図形の描画
def drawing_shapes(img):
    # 描画オブジェクトを作成
    draw = ImageDraw.Draw(img)

    ## 円を描画
    draw.ellipse((20, 20, 50, 50), fill=(255, 0, 0))
    ## 四角形を描画
    draw.rectangle((100, 100, 130, 120), fill=(0, 255, 0))

    img.show()

if __name__ == "__main__":
    pil_main()