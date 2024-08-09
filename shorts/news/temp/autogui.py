# import pyautogui
# import subprocess
# import time
#
# # 스포트라이트 검색을 통해 KakaoTalk 실행
# subprocess.run(['osascript', '-e', 'tell application "System Events" to keystroke space using command down'])
# time.sleep(0.5)
# pyautogui.typewrite('KakaoTalk')
# time.sleep(0.5)
# pyautogui.press('enter')
# time.sleep(5)  # 프로그램이 실행될 때까지 대기
#
# # 로그인 정보 입력
# pyautogui.typewrite('lghan00020@nate.com')
# time.sleep(0.5)
# pyautogui.press('tab')
# time.sleep(0.5)
# pyautogui.typewrite('hyun2131@')
#
# # 로그인 버튼 찾기 및 클릭
# login_button = pyautogui.locateOnScreen('login_button.png', confidence=0.8)
#
# if login_button:
#     button_center = pyautogui.center(login_button)
#     pyautogui.click(button_center)
# else:
#     print("로그인 버튼을 찾을 수 없습니다.")
import pyautogui
import subprocess
import time
from PIL import ImageGrab


# 디버그 로그를 출력하는 함수
def debug_log(message):
    print(f"[DEBUG] {message}")


# 화면 스케일링 비율 계산 함수
def get_screen_scaling():
    screenshot = ImageGrab.grab()
    screen_width, screen_height = screenshot.size
    actual_width, actual_height = pyautogui.size()
    return screen_width / actual_width, screen_height / actual_height


# 스포트라이트 검색을 통해 KakaoTalk 실행
debug_log("Starting KakaoTalk...")
subprocess.run(['osascript', '-e', 'tell application "System Events" to keystroke space using command down'])
time.sleep(0.5)
pyautogui.typewrite('KakaoTalk')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(5)  # 프로그램이 실행될 때까지 대기

# 로그인 정보 입력
debug_log("Entering username...")
pyautogui.typewrite('lghan00020@nate.com')
time.sleep(0.5)
debug_log("Entering password...")
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.typewrite('hyun2131@')

# 추가 대기 시간
time.sleep(2)

# 로그인 버튼 찾기 및 클릭
debug_log("Looking for login button...")
login_button_path = '/temp/login_button.png'
try:
    # 화면 스케일링 비율 계산
    scale_x, scale_y = get_screen_scaling()
    debug_log(f"Screen scaling - X: {scale_x}, Y: {scale_y}")

    # 로그인 버튼 찾기
    login_button = pyautogui.locateOnScreen(login_button_path, confidence=0.8)
    if login_button:
        debug_log("Login button found.")
        button_center = pyautogui.center(login_button)
        debug_log(f"Button center before scaling: {button_center}")

        # 좌표 스케일링 적용
        scaled_center = (button_center[0] / scale_x, button_center[1] / scale_y)
        debug_log(f"Button center after scaling: {scaled_center}")

        # 여러 번 클릭 시도
        for _ in range(3):
            pyautogui.click(scaled_center)
            time.sleep(1)  # 클릭 후 대기 시간

        debug_log("Clicked login button.")
    else:
        debug_log("Login button not found.")
except Exception as e:
    debug_log(f"Error occurred: {e}")
