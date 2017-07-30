#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import copy

# 係数
D = 1.0
# 刻み幅
DY = 1.0
DX = 1.0
DT = 0.2

def main():
    if len(sys.argv) <= 1:
        print('[ERROR] 1st param is image path, 2nd param is final step.')
        sys.exit()
    
    # 画像
    image_path = sys.argv[1]
    # 最終ステップ
    final_step = int(sys.argv[2])

    # 画像読み込み
    image_file = Image.open(image_path)
    image = np.array(image_file)
    plt.title('step {0}'.format(0))
    plt.imshow(image)
    plt.show()
    image = image.astype(np.float)
    # 各種情報取得
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    # 格納先用意
    lap = np.zeros(image.shape)
    image_new = copy.deepcopy(image)
    # 係数用意
    dy2 = DY * DY
    dx2 = DX * DX
    # 計算ループ
    for t in range(1, final_step+1):
        # calculate
        for y in range(height):
            for x in range(width):
                # skip boundary
                if (y == 0) or (y == height - 1) or (x == 0) or (x == width - 1):
                    continue
                for c in range(channel):
                    lap[y][x][c] = (image[y+1][x][c] - 2.0 * image[y][x][c] + image[y-1][x][c]) / dy2 \
                                 + (image[y][x+1][c] - 2.0 * image[y][x][c] + image[y][x-1][c]) / dx2
        # calculate
        for y in range(height):
            for x in range(width):
                for c in range(channel):
                    image_new[y][x][c] = image[y][x][c] + DT * D * lap[y][x][c]
        # バックアップ
        image = copy.deepcopy(image_new)
        # 解を画素値0~255にして表示
        image_show = np.clip(image, 0, 255).astype(np.uint8)
        plt.title('step {0}'.format(t))
        plt.imshow(image_show)
        plt.show()


if __name__ == '__main__':
    main()
