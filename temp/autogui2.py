import os
import platform
import pyautogui
import time


# 디버그 로그를 출력하는 함수
def debug_log(message):
    print(f"[DEBUG] {message}")


# 운영 체제에 따라 프로그램 실행
def run_program(program_name):
    system = platform.system()
    if system == "Windows":
        os.startfile(program_name)
    elif system == "Darwin":  # macOS
        os.system(f'open -a "{program_name}"')


# 프로그램 이름 설정
program_name = "KakaoTalk"

# 프로그램 실행
debug_log(f"Starting {program_name}...")
run_program(program_name)
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
login_button_path = 'login_button.png'  # 로그인 버튼 이미지 경로
try:
    login_button = pyautogui.locateOnScreen(login_button_path, confidence=0.8)
    if login_button:
        debug_log("Login button found.")
        button_center = pyautogui.center(login_button)
        debug_log(f"Button center: {button_center}")

        # 여러 번 클릭 시도
        for _ in range(3):
            pyautogui.click(button_center)
            time.sleep(1)  # 클릭 후 대기 시간

        debug_log("Clicked login button.")
    else:
        debug_log("Login button not found.")
except Exception as e:
    debug_log(f"Error occurred: {e}")
