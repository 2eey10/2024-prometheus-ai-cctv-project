import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

"""
streamlit run run_gui.py
"""

st.title("😄 5팀의 멀티모달 영상분석🚀")
"""
실시간 영상 분석 추론을 시작합니다.
"""
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # OpenCV를 활용한 영상 처리 가능.
    # 그레이스케일로 변환 시:
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
