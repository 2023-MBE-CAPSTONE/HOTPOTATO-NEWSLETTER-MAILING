import os
import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈

from dotenv import load_dotenv

 
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 유효성 검사를 위한 정규표현식
    if re.match(reg, addr):
        smtp.sendmail(hotpotato_gmail_account, addr, msg.as_string())
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("받으실 메일 주소를 정확히 입력하십시오.")

if __name__ == "__main__":
    load_dotenv(verbose=True)
    # smpt 서버와 연결
    gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
    gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
    
    # 로그인
    hotpotato_gmail_account = os.getenv("HOTPOTATO_GMAIL_ACCOUNT")
    hotpotato_gmail_app_password = os.getenv("HOTPOTATO_GMAIL_APP_PASSWORD")
    smtp.login(hotpotato_gmail_account, hotpotato_gmail_app_password)
    
    # 메일을 받을 계정
    to_mail = "seathat33@gmail.com"
    
    # 메일 기본 정보 설정
    msg = MIMEMultipart()
    msg["Subject"] = f"첨부 파일 확인 바랍니다"  # 메일 제목
    msg["From"] = hotpotato_gmail_account
    msg["To"] = to_mail
    in_text = "감자"
    # 메일 본문 내용
    html_body = """
        <html>
        <body>
            <p>{text}</p>
            <p>이것은 추가 텍스트입니다. 원하는 내용을 여기에 추가하세요.</p>
            <p>뉴스레터 내용을 확장하고 원하는 내용을 여기에 추가하세요.</p>
        </body>
        </html>
        """.format(text=in_text)
    content_part = MIMEText(html_body, "html")
    msg.attach(content_part)
    
    # 이미지 파일 추가
    
    # 받는 메일 유효성 검사 거친 후 메일 전송
    sendEmail(to_mail)
    
    # smtp 서버 연결 해제
    smtp.quit()