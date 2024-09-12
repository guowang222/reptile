'''
1、匀变速直线运动的速度与时间关系的公式：V=V0+at
2、匀变速直线运动的位移与时间关系的公式：x=v0t+½at²
'''
def get_track(distance):
    track = [] # 0,1,1,2,2,3,3,4,5,6,7,8,7,5,3,2,1,0
    # 从哪个位置开始滑动
    current = 0
    # 减速的阈值
    mid = distance*4/5
    # 时间
    t = 0.4
    # 速度
    v = 0
    while current < distance:
        if current < mid:
            a = 2 # 加速值
        else:
            a = -3 
        v0 = v
        v = v0 + a * t # 新的移动速度
        move = v0*t +1/2*a*t*t  # 移动的距离
        track.append(round(move)) # 加入移动轨迹
        current += move    # current 记录当前位置
    track.append(distance- sum(track))
    return track

if __name__ == "__main__":
    t , d = get_track(300)
    print(t)