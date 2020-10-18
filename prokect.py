import cv2

if __name__ == '__main__':
    n = int(input())
    path = input()
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    count = 0
    while (cap.isOpened()):
        count += 1
        ret, frame = cap.read()
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        font = cv2.FONT_HERSHEY_SIMPLEX
        up_x = int(frame_width / 2) - 50
        up_y = int(frame_height / 2) - 50
        low_x = int(frame_width / 2) + 50
        low_y = int(frame_height / 2) + 50
        cv2.putText(frame, 'my_rectangle', (up_x - 30, up_y - 10), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (up_x, up_y), (low_x, low_y), (0, 255, 0), 5)
        cv2.imshow('Frame', frame)
        cv2.imwrite(path + "frame" + str(count) + ".png", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        if count > n:
            break
    cap.release()
    cv2.destroyAllWindows()



