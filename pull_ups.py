# pull_ups.py

# Сторонние модули
import cv2
import mediapipe as mp

async def check_pull(name:str):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    
    cap = cv2.VideoCapture(f"cvmedia/{name}")
     
    count = -1
    position = None
     
    with mp_pose.Pose(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as pose:
     
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break        

            image.flags.writeable = True
            results = pose.process(image)
            imlist=[]
        
        
            if (results.pose_landmarks != None):
                mp_drawing.draw_landmarks(image,
                                        results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                for id,im in enumerate(results.pose_landmarks.landmark):
                    h,w,_=image.shape
                    X,Y=int(im.x*w), int(im.y*h)
                    imlist.append([id,X,Y])
                if (len(imlist)!=0):
        
                    if (
                            (imlist[12][2]  < imlist[14][2] and imlist[11][2]  < imlist[13][2])
                        and 
                            (imlist[4][2]  < imlist[16][2] and imlist[1][2]  < imlist[15][2])
                        ):
                        position="down"
        
                    elif (
                            (imlist[12][2]  >= imlist[14][2] and imlist[11][2]  >= imlist[13][2])
                        and 
                            (imlist[4][2]  >= imlist[16][2] and imlist[1][2]  >= imlist[15][2])
                        and position=="down"
                        ):
        
                        position="up"
                        count+=1

    return count
