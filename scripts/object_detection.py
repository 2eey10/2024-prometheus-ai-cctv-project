import cv2
import torch
import time
import os
import shutil

def object_detection():
    """
    YOLOv5를 사용하여 웹캠에서 객체 탐지를 수행하는 함수.
    """
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    # 모델 저장 경로 설정
    os.environ['TORCH_HOME'] = './models'  

    # 모델 로드
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # .pt 파일 이동
    source_pt_path = './yolov5s.pt'  
    target_pt_dir = './models'       
    target_pt_path = os.path.join(target_pt_dir, 'yolov5s.pt')
    if os.path.exists(source_pt_path):
        if not os.path.exists(target_pt_dir):
            os.makedirs(target_pt_dir)
        shutil.move(source_pt_path, target_pt_path)
    else:
        pass
    
    # 객체 탐지 실행    
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        results.render()
        df = results.pandas().xyxy[0]
        counts = df['name'].value_counts()
        current_time = time.strftime("%Y년 %m월 %d일 %H:%M:%S", time.localtime())
        detection_message = ", ".join([f"{cls} {cnt}" for cls, cnt in counts.items()])
        print(f"현재 시간 {current_time}, {detection_message}이(가) 탐지되었습니다.")
        cv2.imshow('YOLOv5 Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
