import cv2, time, pandas
from datetime import datetime

df=pandas.DataFrame(columns=["start", "end"])
first_frame=None
status_list=[None, None]
times = []

video = cv2.VideoCapture(0)
while True:
    status = 0
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #remove noise
    gray-cv2.GaussianBlur(gray, (21,21), 0)
    if first_frame is None:
        first_frame = gray
        continue

    #create the differences between the background frame and the new captured ones
    delta_frame=cv2.absdiff(first_frame, gray)
    #if delta is higher than 40 than the "spots" are whitened while the rest are "blackened"
    tsh_frame = cv2.threshold(delta_frame, 40, 255, cv2.THRESH_BINARY)[1]
    #smooth the white spots
    tsh_frame=cv2.dilate(tsh_frame, None, iterations=2)
    #look for "white spots"
    (cnts, _) = cv2.findContours(tsh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        #if the area of those white spots is "large enough" than there's definitely movement there so proceed to
        #change status (it detected movement)
        status = 1
        #plot rectangle)
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
    status_list.append(status)
    #memory management (keeping only the last two start,end values)
    status_list=status_list[-2:]
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    
    cv2.imshow("Gray...", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("ThreshHold", tsh_frame)
    cv2.imshow("CAPTURING...", frame)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break
print(status_list)
print(times)
for i in range(0, len(times), 2):
    df=df.append({"start": times[i], "end": times[i+1]}, ignore_index=True)

df.to_csv("TimesMovement.csv")
video.release()
cv2.destroyAllWindows
