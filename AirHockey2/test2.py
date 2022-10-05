
import cv2
import mediapipe as mp
#def te():
vid = cv2.VideoCapture(0)
#width, height, _ = 1150, 600
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1150)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
mphands = mp.solutions.hands
Hands = mphands.Hands(max_num_hands= 2, min_detection_confidence= 0.7, min_tracking_confidence= 0.6 )
ret = []
    #mpdraw = mp.solutions.drawing_utils


p1_x = 1150/4
p2_x =  3*1150/4
p1_y = 600/2
p2_y = 600/2
while True :
    _,frame = vid.read()
        # convert from bgr to rgb
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    RGBframe = cv2.flip(RGBframe,1)
    result = Hands.process(RGBframe)
    p1_x_change = 0
    p2_x_change = 0
    p1_y_change = 0
    p2_y_change = 0
    if result.multi_hand_landmarks:
        for handLm in result.multi_hand_landmarks :
            for id, lm in enumerate(handLm.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 0:
                    if cx > w/2: # p2
                        p2_x_change = cx - p2_x
                        p2_x = cx
                    else: # p1
                        p1_x_change = cx - p1_x
                        p1_x = cx
                if id == 2:
                    if cx > w/2: # p2
                        p2_y_change = cy - p2_y
                        p2_y = cy
                    else: # p1
                        p1_y_change = cy - p1_y
                        p1_y = cy
                else :
                    pass

    w = s = a = d = False
    up = down = left = right = False

    if p1_x_change > 5:
        d = True
    elif p1_x_change < -5:
        a = True
    else:
        pass
    if p1_y_change < -5:
        w = True
    elif p1_y_change > 5:
        s = True
    else:
        pass

    if p2_x_change > 5:
        right = True
    elif p2_x_change < -5:
        left = True
    else:
        pass
    if p2_y_change < -5:
        up = True
    elif p2_y_change > 5:
        down = True
    else:
        pass
    cv2.waitKey(1)
    print("[p1] = [", w, ",", s, ",", a, ",", d, "]", "\t[p2] = [", up, ",", down, ",", left, ",", right, "]")
    #cv2.imshow("rgbvideo", RGBframe)
    cv2.imshow("video", frame)
    #if len(ret)==4:
    #    break;
    #else:
    #    ret.clear()
    #cv2.waitKey(33)
print(ret)
