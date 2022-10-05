
import cv2
import mediapipe as mp
#def te():
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1150)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
mphands = mp.solutions.hands
Hands = mphands.Hands(max_num_hands= 2, min_detection_confidence= 0.7, min_tracking_confidence= 0.6 )
ret = []
    #mpdraw = mp.solutions.drawing_utils
while True :
    _,frame = vid.read()
        # convert from bgr to rgb
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    RGBframe = cv2.flip(RGBframe,1)
    result = Hands.process(RGBframe)
    if result.multi_hand_landmarks:
            #print("hand found")
        for handLm in result.multi_hand_landmarks :
                    #print(handLm)
                    #mpdraw.draw_landmarks(frame, handLm, mphands.HAND_CONNECTIONS,
                    #                      mpdraw.DrawingSpec(color=(0, 0, 255), circle_radius=7,
                    #                                         thickness=cv2.FILLED),
                    #                      mpdraw.DrawingSpec(color=(0, 255, 0), thickness=7)
                    #                      )
            for id, lm in enumerate(handLm.landmark):
                h, w, _ = frame.shape
                        #cx, cy = int(lm.x * w), int(lm.y * h)
                if(id == 0 ):
                    print(lm.x, " " , lm.y)
                    #ret.append(lm.x)
                #if(id == 2):

                    #ret.append(lm.y)
                else :
                    pass

    #cv2.imshow("rgbvideo", RGBframe)
    cv2.imshow("video", frame)
    #if len(ret)==4:
    #    break;
    #else:
    #    ret.clear()
    cv2.waitKey(1)
print(ret)
