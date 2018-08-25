# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 09:44:02 2018

@author: Peter
"""
import cv2
import numpy as np

hand_hist = None
traverse_point = []
total_rectangle = 9
hand_rect_one_x = None
hand_rect_one_y = None

hand_rect_two_x = None
hand_rect_two_y = None

'''
按比例调整图像大小，默认比例为1.3
'''
def rescale_frame(frame, wpercent=130, hpercent=130):
    width = int(frame.shape[1] * wpercent / 100)
    height = int(frame.shape[0] * hpercent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

"""
获取轮廓参数
"""
def contours(hist_mask_image):
    # 转换为单通道图像
    gray_hist_mask_image = cv2.cvtColor(hist_mask_image, cv2.COLOR_BGR2GRAY)
    # cv2.threshold (源图片, 阈值, 填充色, 阈值类型)
    ret, thresh = cv2.threshold(gray_hist_mask_image, 80, 255, 3)
    _, cont, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return cont


def max_contour(contour_list):
    max_i = 0
    max_area = 0

    for i in range(len(contour_list)):
        cnt = contour_list[i]

        area_cnt = cv2.contourArea(cnt)

        if area_cnt > max_area:
            max_area = area_cnt
            max_i = i

        return contour_list[max_i]

'''
在输入框架中绘制样本提取框
frame：输入框架图形
返回：
1.绘制完提取框的图像框架
2.全局变量：
  total_rectangle：提取矩形数量
  hand_rect_one_x,hand_rect_one_y：矩形框左上点坐标
  hand_rect_two_x,hand_rect_two_y：矩形框右下点坐标
'''
def draw_rect(frame):
    global total_rectangle, hand_rect_one_x, hand_rect_one_y, hand_rect_two_x, hand_rect_two_y
    rows, cols, _ = frame.shape # 框架大小
    
    hand_rect_one_x = np.array(
        [6 * rows / 20, 6 * rows / 20, 6 * rows / 20, 9 * rows / 20, 9 * rows / 20, 9 * rows / 20, 12 * rows / 20,
         12 * rows / 20, 12 * rows / 20], dtype=np.uint32)

    hand_rect_one_y = np.array(
        [9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20,
         10 * cols / 20, 11 * cols / 20], dtype=np.uint32)

    hand_rect_two_x = hand_rect_one_x + 10
    hand_rect_two_y = hand_rect_one_y + 10

    for i in range(total_rectangle):
        cv2.rectangle(frame, (hand_rect_one_y[i], hand_rect_one_x[i]),
                      (hand_rect_two_y[i], hand_rect_two_x[i]),
                      (0, 255, 0), 1)

    return frame

"""
提取兴趣对象样本转换成HSV直方图:
frame：输入图像框架
hand_rect_one_x,hand_rect_one_y：兴趣对象提取矩形框阵列位置
total_rectangle：提取矩形框总数量
返回：样本直方图矩阵
注意：
    使用时，样本应当尽量占据采样矩形阵列！
"""
def hand_histogram(frame):
    global hand_rect_one_x, hand_rect_one_y
    # 转换成HSV格式图像
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 使用numpy生成[90*10]颜色通道3的矩阵空间，从矩形采样阵列中提取900个像素点保存。
    roi = np.zeros([90, 10, 3], dtype=hsv_frame.dtype)
    for i in range(total_rectangle):
        roi[i * 10: i * 10 + 10, 0: 10] = hsv_frame[hand_rect_one_x[i]:hand_rect_one_x[i] + 10,
                                          hand_rect_one_y[i]:hand_rect_one_y[i] + 10]
    # 计算[roi]样本矩阵的直方图，并对矩阵归一化返回
    hand_hist = cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
    return cv2.normalize(hand_hist, hand_hist, 0, 255, cv2.NORM_MINMAX)

'''
直方图反向投射函数
frame：需要反向投射的输入图像
hist：感兴趣对象的图像直方图
输出：找到的对象
'''
def hist_masking(frame, hist):
#    frame=cv2.medianBlur(frame,3) # 可选滤波
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 计算反向投影概率图,色调0～180，饱和度0～256
    dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)
    # 定义椭圆结构元素31X31，以便使用圆盘卷积。
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    # 应用圆盘卷积 dst=dst*disc
    cv2.filter2D(dst, -1, disc, dst)
    # 可选滤波
#    gaussian_ksize=11
#    gaussian_sigma=0
#    median_ksize=3
#    dst = cv2.GaussianBlur(dst,(gaussian_ksize,gaussian_ksize),gaussian_sigma)
#    dst = cv2.medianBlur(dst,median_ksize) 
    # 阈值、二进制按位和操作    
    hsv_thresh_lower=50      
    ret, thresh = cv2.threshold(dst, hsv_thresh_lower, 255, cv2.THRESH_BINARY) 
    thresh = cv2.merge((thresh, thresh, thresh))
    return cv2.bitwise_and(frame, thresh)
  
def centroid(max_contour):
    moment = cv2.moments(max_contour)
    if moment['m00'] != 0:
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])
        return cx, cy
    else:
        return None


def farthest_point(defects, contour, centroid):
    if defects is not None and centroid is not None:
        s = defects[:, 0][:, 0]
        cx, cy = centroid

        x = np.array(contour[s][:, 0][:, 0], dtype=np.float)
        y = np.array(contour[s][:, 0][:, 1], dtype=np.float)

        xp = cv2.pow(cv2.subtract(x, cx), 2)
        yp = cv2.pow(cv2.subtract(y, cy), 2)
        dist = cv2.sqrt(cv2.add(xp, yp))

        dist_max_i = np.argmax(dist)

        if dist_max_i < len(s):
            farthest_defect = s[dist_max_i]
            farthest_point = tuple(contour[farthest_defect][0])
            return farthest_point
        else:
            return None


def draw_circles(frame, traverse_point):
    if traverse_point is not None:
        for i in range(len(traverse_point)):
            cv2.circle(frame, traverse_point[i], int(5 - (5 * i * 3) / 100), [0, 255, 255], -1)


def manage_image_opr(frame, hand_hist):
    hist_mask_image = hist_masking(frame, hand_hist)
    contour_list = contours(hist_mask_image)
    max_cont = max_contour(contour_list)

    cnt_centroid = centroid(max_cont)
    cv2.circle(frame, cnt_centroid, 5, [255, 0, 255], -1)

    if max_cont is not None:
        hull = cv2.convexHull(max_cont, returnPoints=False)
        defects = cv2.convexityDefects(max_cont, hull)
        far_point = farthest_point(defects, max_cont, cnt_centroid)
        print("Centroid : " + str(cnt_centroid) + ", farthest Point : " + str(far_point))
        cv2.circle(frame, far_point, 5, [0, 0, 255], -1)
        if len(traverse_point) < 20:
            traverse_point.append(far_point)
        else:
            traverse_point.pop(0)
            traverse_point.append(far_point)

        draw_circles(frame, traverse_point)

'''
图像去除背景操作
frame：输入框架图像
model：背景去除模型
返回：去除背景厚的图像
'''
def bg_remove(frame,model):
    fg_mask=bg_model.apply(frame)
    kernel = np.ones((1,1),np.uint8)
    fg_mask=cv2.erode(fg_mask,kernel,iterations = 1)
    frame=cv2.bitwise_and(frame,frame,mask=fg_mask)
    return frame

def test():
    import copy
    
    capture_flag = 0    # 感兴趣对象预定义捕捉请求标志
    capture_done = 0    # 感兴趣对象捕捉完成标志
    cap = cv2.VideoCapture(0)
    # 背景抽离对象（可选）
#    bg_model = cv2.createBackgroundSubtractorMOG2(0,10) 
    cv2.namedWindow('orgin')
    cv2.namedWindow('test')
    while cap.isOpened():
        _,frame_raw = cap.read()
        # 尺寸改变
        frame_rescale = rescale_frame(frame_raw)
        # 产生副本
        frame = copy.copy(frame_rescale)
        # 双边滤波（可选）
#        frame=cv2.bilateralFilter(frame,5,50,100)     
        # 获取轮廓参数
        #conts = contours(frame)
        # 绘制轮廓
        #cv2.drawContours(frame, conts, -1, (255, 0, 255), 3)
        # 去除背景（可选）
#        frame = bg_remove(frame,bg_model)
        ## 反向投影测试
        # 计算兴趣对象直方图对象
        if(capture_flag):
#            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#            roi = np.zeros([100, 100, 3], dtype=hsv_frame.dtype)
#    
#            for i in range(total_rectangle):
#                roi[0:100, 0:100] = hsv_frame[0:100,0:100]
#            hist = cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
#            cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
            # 使用采样矩阵采样
            hist = hand_histogram(frame)
            capture_flag = 0
            capture_done = 1
        
        if(capture_done):
            # 滤波和边界计算    
            frame_test = hist_masking(frame, hist)
        else:
            frame_test = copy.copy(frame)
            #cv2.rectangle(frame_test,(0,100),(100,0),(255,0,0),3)
            draw_rect(frame_test)
        # 显示图像
        cv2.imshow("orgin", frame)
        cv2.imshow("test", frame_test)
        # 接收指令
        key=cv2.waitKey(100)
        if key==ord('q') or key==ord('Q'):
            break
        if key==ord('c') or key==ord('C'):
            capture_flag = 1
            capture_done = 0
        if key==ord('r') or key==ord('R'):
            capture_flag = 0
            capture_done = 0
    # 关闭摄像头及窗口
    cap.release()
    cv2.destroyAllWindows()   
## 测试代码
if __name__ == '__main__':
    test()
