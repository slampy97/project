import cv2
import argparse
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger_handler = logging.FileHandler('python_logging.log')
logger_handler.setLevel(logging.INFO)

def argparse_part():
    parser = argparse.ArgumentParser(description='Videos to frames')
    parser.add_argument('video_path', type =str, help="input path of video file")
    logger.info('Добавлен аргумент путь в видеофайлу')
    parser.add_argument('fr_number', type=int, help='Input number of frames')
    logger.info('Добавлен аргумент количество кадров')
    parser.add_argument('outdir', type=str, help='Output dir for image')
    logger.info('Добавлен аргумент выходной директории')
    args = parser.parse_args()
    n = args.fr_number
    path = args.outdir
    video_path = args.video_path
    logger.info('все 3 аргумента считаны и переданы далее')
    return video_path, n, path

def video_handle(n, video_path, path):
    logger.info('Обращение к видеофайлу')
    cap = cv2.VideoCapture(video_path, cv2.CAP_DSHOW)
    logger.info('Начало считывая видеофайла')
    count = 0
    while (cap.isOpened()):
        logger.info('считывание кадра номер ' + str(count))
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
            logger.info('Конец считывания видеофайла')
            break

    cap.release()
    logger.info('Освобождение захвата видефайла')
    cv2.destroyAllWindows()
    logger.info('Освобождение всех прочих ресурсов')

def main():
    video_path, n, path = argparse_part()
    video_handle(n, video_path, path)

main()


