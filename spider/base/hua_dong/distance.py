# pip install opencv-python
# pip install streamlit
import cv2
# import streamlit as st

def get_long():
    # 导入图片
    img1 = cv2.imread('./imgs/cpt1.png')
    img2 = cv2.imread('./imgs/cpt2.png')

    # 建立2个 st 控制的变量
    # min_value = st.slider('input min value',max_value=500)
    # max_value = st.slider('input max value',max_value=1000)
    # 边缘化图片
    # Canny使用的滞后阈值，低阈值，高阈值
    # canny1 = cv2.Canny(img1,min_value,max_value)
    canny1 = cv2.Canny(img1,350,850)
    # 保存图片
    cv2.imwrite('./imgs/tcpt1.png',canny1)

    # 使用 streamlit 输出结果
    # st.image(canny1)
    # st.write(canny1)

    canny2 = cv2.Canny(img2,350,850)
    cv2.imwrite('./imgs/tcpt2.png',canny2)

    # st.image(canny2)

    # 加载边缘化后的图片
    big = cv2.imread('./imgs/tcpt1.png')
    small = cv2.imread('./imgs/tcpt2.png')
    # 对比图片
    rs = cv2.matchTemplate(big, small, cv2.TM_CCORR_NORMED)
    # 通过制定的方法来查询相应的结果
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(rs)
    # st.write(rs)
    # st.write(min_val, max_val, min_loc, max_loc)
    # st.write(big.shape)
    return max_loc[0]/big.shape[1]*340
    
    '''
    # 画图个框来验证，匹配的结果是否正确
    tw,th = small.shape[:2]
    timg = cv2.rectangle(big, max_loc, (max_loc[0]+tw,max_loc[1]+th), (255,255,0))
    st.image(timg)
    '''
if __name__ == '__main__':
    get_long()