import sys
import you_get  # 依赖库


def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()


#
# if __name__ == '__main__':
#     # 视频网站的地址
#     for i in range(77, 17, -1):
#         url = 'https://www.bilibili.com/video/BV1NU4y1M7rF/?p=' + str(i)
#         # 视频输出的位置
#         path = 'E:\算法flv'
#         download(url, path)

if __name__ == '__main__':
    # 视频网站的地址
    url = 'https://www.bilibili.com/video/BV1NU4y1M7rF/?p=35'

    # url = 'https://www.bilibili.com/video/BV1Hc411P7nN/?spm_id_from=333.1007.tianma.1-2-2.click'
    # 视频输出的位置
    path = r'D:\yolov5_test\黑马程序员\视频下载'
    download(url, path)
