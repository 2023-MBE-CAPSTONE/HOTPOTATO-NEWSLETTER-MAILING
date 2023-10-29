import os
import smtplib  
import re  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  

from dotenv import load_dotenv

 
def send_email(email_address):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  
    if re.match(reg, email_address):
        smtp.sendmail(hotpotato_gmail_account, email_address, msg.as_string())
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("받으실 메일 주소를 정확히 입력하십시오.")

if __name__ == "__main__":
    load_dotenv(verbose=True)
    gmail_smtp = "smtp.gmail.com"  
    gmail_port = 465  
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
    
    hotpotato_gmail_account = os.getenv("HOTPOTATO_GMAIL_ACCOUNT")
    hotpotato_gmail_app_password = os.getenv("HOTPOTATO_GMAIL_APP_PASSWORD")
    smtp.login(hotpotato_gmail_account, hotpotato_gmail_app_password)
    
    to_mail = "seathat33@gmail.com"
    
    msg = MIMEMultipart()
    msg["Subject"] = f"첨부 파일 확인 바랍니다"  
    msg["From"] = hotpotato_gmail_account
    msg["To"] = to_mail
    in_text = "감자"
    # 메일 본문 내용
    html_body = """
        <!doctype html>
            <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
            <head>
            <title></title>
            <!--[if !mso]><!-->
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <!--<![endif]-->
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style type="text/css">
            #outlook a{padding:0;}body{margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}table,td{border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;}img{border:0;height:auto;line-height:100%;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;}p{display:block;margin:0;}
            </style>
            <!--[if mso]> <noscript><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
            <![endif]-->
            <!--[if lte mso 11]>
            <style type="text/css">
            .ogf{width:100% !important;}
            </style>
            <![endif]-->
            <!--[if !mso]><!-->
            <link href="https://fonts.googleapis.com/css?family=Inter:400,700" rel="stylesheet" type="text/css">
            <style type="text/css">

            </style>
            <!--<![endif]-->
            <style type="text/css">
            @media only screen and (min-width:599px){.xc542{width:542px!important;max-width:542px;}.xc26{width:26px!important;max-width:26px;}.xc568{width:568px!important;max-width:568px;}.xc290{width:290px!important;max-width:290px;}.xc8{width:8px!important;max-width:8px;}.xc270{width:270px!important;max-width:270px;}.xc280{width:280px!important;max-width:280px;}.pc100{width:100%!important;max-width:100%;}.pc48-5075{width:48.5075%!important;max-width:48.5075%;}.pc2-9851{width:2.9851%!important;max-width:2.9851%;}}
            </style>
            <style media="screen and (min-width:599px)">.moz-text-html .xc542{width:542px!important;max-width:542px;}.moz-text-html .xc26{width:26px!important;max-width:26px;}.moz-text-html .xc568{width:568px!important;max-width:568px;}.moz-text-html .xc290{width:290px!important;max-width:290px;}.moz-text-html .xc8{width:8px!important;max-width:8px;}.moz-text-html .xc270{width:270px!important;max-width:270px;}.moz-text-html .xc280{width:280px!important;max-width:280px;}.moz-text-html .pc100{width:100%!important;max-width:100%;}.moz-text-html .pc48-5075{width:48.5075%!important;max-width:48.5075%;}.moz-text-html .pc2-9851{width:2.9851%!important;max-width:2.9851%;}
            </style>
            <style type="text/css">
            @media only screen and (max-width:598px){table.fwm{width:100%!important;}td.fwm{width:auto!important;}}noinput.mn-checkbox{display:block!important;max-height:none!important;visibility:visible!important;}
            @media only screen and (max-width:598px){.mn-checkbox[type="checkbox"]~.il{display:none!important;}.mn-checkbox[type="checkbox"]:checked~.il,.mn-checkbox[type="checkbox"]~.mn-trigger{display:block!important;max-width:none!important;max-height:none!important;font-size:inherit!important;}.mn-checkbox[type="checkbox"]~.il>a{display:block!important;}.mn-checkbox[type="checkbox"]:checked~.mn-trigger .mn-icon-close{display:block!important;}.mn-checkbox[type="checkbox"]:checked~.mn-trigger .mn-icon-open{display:none!important;}}
            </style>
            <style type="text/css">
            u+.emailify .gs{background:#000;mix-blend-mode:screen;display:inline-block;padding:0;margin:0;}u+.emailify .gd{background:#000;mix-blend-mode:difference;display:inline-block;padding:0;margin:0;}p{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;}u+.emailify a{color:inherit!important;text-decoration:none!important;}#MessageViewBody a{color:inherit!important;text-decoration:none!important;}td.b .klaviyo-image-block{display:inline;vertical-align:middle;}
            @media only screen and (max-width:599px){.emailify{height:100%!important;margin:0!important;padding:0!important;width:100%!important;}u+.emailify .glist{margin-left:1em!important;}td.ico.v>div.il>a.l.m,td.ico.v .mn-label{padding-right:0!important;padding-bottom:16px!important;}td.x{padding-left:0!important;padding-right:0!important;}.fwm img{max-width:100%!important;height:auto!important;}.aw img{width:auto!important;margin-left:auto!important;margin-right:auto!important;}.awl img{width:auto!important;margin-right:auto!important;}.awr img{width:auto!important;margin-left:auto!important;}.ah img{height:auto!important;}td.b.nw>table,td.b.nw a{width:auto!important;}td.stk{border:0!important;}td.u{height:auto!important;}br.sb{display:none!important;}.thd-1 .i-thumbnail{display:inline-block!important;height:auto!important;overflow:hidden!important;}.hd-1{display:block!important;height:auto!important;overflow:visible!important;}.hm-1{display:none!important;max-width:0!important;max-height:0!important;overflow:hidden!important;mso-hide:all!important;}.ht-1{display:table!important;height:auto!important;overflow:visible!important;}.hr-1{display:table-row!important;height:auto!important;overflow:visible!important;}.hc-1{display:table-cell!important;height:auto!important;overflow:visible!important;}div.r.pr-16>table>tbody>tr>td,div.r.pr-16>div>table>tbody>tr>td{padding-right:16px!important}div.r.pl-16>table>tbody>tr>td,div.r.pl-16>div>table>tbody>tr>td{padding-left:16px!important}div.r.s-24>table>tbody>tr>td>div.gtr>table>tbody>tr>td{padding-top:0!important;padding-right:0!important;padding-bottom:24px!important;padding-left:0!important;}td.b.fw-1>table{width:100%!important}td.fw-1>table>tbody>tr>td>a{display:block!important;width:100%!important;padding-left:0!important;padding-right:0!important;}td.b.fw-1>table{width:100%!important}td.fw-1>table>tbody>tr>td{width:100%!important;padding-left:0!important;padding-right:0!important;}div.g.mb-24>table>tbody>tr>td{padding-bottom:24px!important}div.w.pr-16>table>tbody>tr>td,div.w.pr-16>div>table>tbody>tr>td{padding-right:16px!important;}div.w.pl-16>table>tbody>tr>td,div.w.pl-16>div>table>tbody>tr>td{padding-left:16px!important;}td.v.s-8>div.il>a.l.m{padding-right:8px!important;}td.v.ico.s-8>div.il>a.l.m,td.v.ico.s-8 .mn-label{padding-bottom:8px!important;padding-right:0!important;}}
            @media (prefers-color-scheme:light) and (max-width:599px){.ds-1.hd-1{display:none!important;height:0!important;overflow:hidden!important;}}
            @media (prefers-color-scheme:dark) and (max-width:599px){.ds-1.hd-1{display:block!important;height:auto!important;overflow:visible!important;}}
            </style>
            <meta name="color-scheme" content="light dark">
            <meta name="supported-color-schemes" content="light dark">
            <!--[if gte mso 9]>
            <style>a:link,span.MsoHyperlink{mso-style-priority:99;color:inherit;text-decoration:none;}a:visited,span.MsoHyperlinkFollowed{mso-style-priority:99;color:inherit;text-decoration:none;}li{text-indent:-1em;}table,td,p,div,span,ul,ol,li,a{mso-hyphenate:none;}sup,sub{font-size:100% !important;}
            </style>
            <![endif]-->
            </head>
            <body lang="en" link="#DD0000" vlink="#DD0000" class="emailify" style="mso-line-height-rule:exactly;mso-hyphenate:none;word-spacing:normal;background-color:#f5f5f5;"><div class="bg" style="background-color:#f5f5f5;" lang="en">
            <!--[if mso | IE]>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="r  pr-16 pl-16" style="background:#fffffe;background-color:#fffffe;margin:0px auto;max-width:600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#fffffe;background-color:#fffffe;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="c-outlook -outlook -outlook" style="vertical-align:middle;width:542px;">
            <![endif]--><div class="xc542 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="center" class="i" style="font-size:0;padding:0;word-break:break-word;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0;"><tbody><tr><td style="width:277px;"> <img alt src="img/c42bd4459102d34502019b8a4e0912d2.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" title width="277" height="auto">
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td class="" style="width:26px;">
            <![endif]--><div class="xc26 ogf" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="r  pr-16 pl-16" style="background:#eeeeee;background-color:#eeeeee;margin:0px auto;max-width:600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#eeeeee;background-color:#eeeeee;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="c-outlook -outlook -outlook" style="vertical-align:middle;width:568px;">
            <![endif]--><div class="xc568 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="background-color:#fffffe;border:none;vertical-align:middle;padding:40px 32px 40px 32px;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody><tr><td align="center" class="x  m" style="font-size:0;padding-bottom:8px;word-break:break-word;"><div style="text-align:center;"><p style="Margin:0;text-align:center;mso-line-height-alt:24px;mso-ansi-font-size:16px;"><span style="font-size:16px;font-family:'Inter',Arial,sans-serif;font-weight:400;color:#dac400;line-height:150%;mso-line-height-alt:24px;mso-ansi-font-size:16px;">정치 / 사회</span></p></div>
            </td></tr><tr><td align="left" class="x  m" style="font-size:0;padding-bottom:8px;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:32px;mso-ansi-font-size:28px;"><span style="font-size:28px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:114%;mso-line-height-alt:32px;mso-ansi-font-size:28px;">Experience our sushi bar</span></p></div>
            </td></tr><tr><td align="left" class="x" style="font-size:0;padding-bottom:0;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:24px;mso-ansi-font-size:16px;"><span style="font-size:16px;font-family:'Inter',Arial,sans-serif;font-weight:400;color:#777777;line-height:150%;mso-line-height-alt:24px;mso-ansi-font-size:16px;">Our sushi bar has some amazing sushi with great variety, as well as dishes from other Asian regions including Korea, Japan, Thailand and Cambodia. We get our ingredients from local producers whenever possible.</span></p></div>
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="r-outlook -outlook pr-16-outlook pl-16-outlook s-24-outlook -outlook" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="r  pr-16 pl-16 s-24" style="background:#fffffe;background-color:#fffffe;margin:0px auto;max-width:600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#fffffe;background-color:#fffffe;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="m-outlook c-outlook -outlook -outlook" style="vertical-align:middle;width:290px;">
            <![endif]--><div class="xc290 ogf m c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="left" class="x  m" style="font-size:0;padding-bottom:8px;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:22px;mso-ansi-font-size:18px;"><span style="font-size:17px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:124%;mso-line-height-alt:22px;mso-ansi-font-size:18px;">Amazingly delicious hand crafted sushi</span></p></div>
            </td></tr><tr><td align="left" class="x  m" style="font-size:0;padding-bottom:8px;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:22px;mso-ansi-font-size:14px;"><span style="font-size:14px;font-family:'Inter',Arial,sans-serif;font-weight:400;color:#777777;line-height:150%;mso-line-height-alt:22px;mso-ansi-font-size:14px;">The finest sushi in Japan, the way it&rsquo;s meant to be eaten, is unadorned, like a flower. It&rsquo;s whole, unadorned, it&rsquo;s just good sushi.</span></p></div>
            </td></tr><tr><td align="left" vertical-align="middle" class="b  fw-1" style="font-size:0;padding:0;padding-bottom:0;word-break:break-word;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;width:246px;line-height:100%;"><tbody><tr><td align="center" bgcolor="transparent" role="presentation" style="border:none;border-radius:3px 3px 3px 3px;cursor:auto;mso-padding-alt:0;background:transparent;" valign="middle"> <a href="#insertUrlLink" style="display:inline-block;width:246px;background:transparent;color:#ffffff;font-family:'Inter',Arial,sans-serif;font-size:13px;font-weight:normal;line-height:100%;margin:0;text-decoration:none;text-transform:none;padding:0;mso-padding-alt:0;border-radius:3px 3px 3px 3px;" target="_blank"> <span style="font-size:14px;font-family:'Inter',Arial,sans-serif;font-weight:400;color:#000000;line-height:121%;text-decoration:underline;mso-line-height-alt:18px;mso-ansi-font-size:14px;">Learn More</span></a>
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td class="g-outlook mb-24-outlook" style="width:8px;">
            <![endif]--><div class="xc8 ogf g mb-24" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td class="c-outlook -outlook -outlook" style="vertical-align:middle;width:270px;">
            <![endif]--><div class="xc270 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td vertical-align="top" class="c" style="font-size:0;word-break:break-word;"><div class="xc280 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:top;" width="100%"><tbody><tr><td align="left" class="x  m" style="font-size:0;padding-bottom:8px;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:22px;mso-ansi-font-size:18px;"><span style="font-size:17px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:124%;mso-line-height-alt:22px;mso-ansi-font-size:18px;">Amazingly delicious hand crafted sushi</span></p></div>
            </td></tr><tr><td align="left" class="x  m" style="font-size:0;padding-bottom:8px;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:22px;mso-ansi-font-size:14px;"><span style="font-size:14px;font-family:'Inter',Arial,sans-serif;font-weight:400;color:#777777;line-height:150%;mso-line-height-alt:22px;mso-ansi-font-size:14px;">The finest sushi in Japan, the way it&rsquo;s meant to be eaten, is unadorned, like a flower. It&rsquo;s whole, unadorned, it&rsquo;s just good sushi.</span></p></div>
            </td></tr><tr><td align="left" vertical-align="middle" class="b  fw-1" style="font-size:0;padding:0;padding-bottom:0;word-break:break-word;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;width:246px;line-height:100%;"><tbody><tr><td align="center" bgcolor="transparent" role="presentation" style="border:none;border-radius:3px 3px 3px 3px;cursor:auto;mso-padding-alt:0;background:transparent;" valign="middle"> <a href="#insertUrlLink" style="display:inline-block;width:246px;background:transparent;color:#ffffff;font-family:'Inter',Arial,sans-serif;font-size:13px;font-weight:normal;line-height:100%;margin:0;text-decoration:none;text-transform:none;padding:0;mso-padding-alt:0;border-radius:3px 3px 3px 3px;" target="_blank"> <span style="font-size:14px;font-family:'Inter',Arial,sans-serif;font-weight:400;color:#000000;line-height:121%;text-decoration:underline;mso-line-height-alt:18px;mso-ansi-font-size:14px;">Learn More</span></a>
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="w-outlook -outlook pr-16-outlook pl-16-outlook -outlook" role="presentation" style="width:600px;" width="600" bgcolor="#fffffe"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="w  pr-16 pl-16" style="background:#fffffe;background-color:#fffffe;margin:0px auto;max-width:600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#fffffe;background-color:#fffffe;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:center;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" width="600px">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" role="presentation" style="width:568px;" width="568"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="r  pr-16 pl-16" style="background:#eeeeee;background-color:#eeeeee;margin:0px auto;border-radius:4px 4px 4px 4px;max-width:568px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#eeeeee;background-color:#eeeeee;width:100%;border-radius:4px 4px 4px 4px;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="width:536px;">
            <![endif]--><div class="pc100 ogf" style="font-size:0;line-height:0;text-align:left;display:inline-block;width:100%;direction:ltr;">
            <!--[if mso | IE]>
            <table border="0" cellpadding="0" cellspacing="0" role="presentation"><tr><td style="vertical-align:middle;width:260px;">
            <![endif]--><div class="pc48-5075 ogf m c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:48.5075%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="left" class="x" style="font-size:0;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:22px;mso-ansi-font-size:18px;"><span style="font-size:17px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:124%;mso-line-height-alt:22px;mso-ansi-font-size:18px;">Amazingly delicious hand crafted sushi</span></p></div>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td style="width:16px;">
            <![endif]--><div class="pc2-9851 ogf g" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:2.9851%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td style="vertical-align:middle;width:260px;">
            <![endif]--><div class="pc48-5075 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:48.5075%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="right" class="i" style="font-size:0;padding:0;word-break:break-word;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0;"><tbody><tr><td style="width:44px;"> <img alt src="img/e46a6d60b80e2794caf3b449151c2489.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" title width="44" height="auto">
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]--></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            </td></tr><tr><td class="" width="600px">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:568px;" width="568"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div style="margin:0px auto;max-width:568px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;"><tbody><tr><td style="direction:ltr;font-size:0;padding:0;text-align:center;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="width:568px;">
            <![endif]--><div class="pc100 ogf" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody><tr><td class="s" style="font-size:0;padding:0;word-break:break-word;" aria-hidden="true"><div style="height:8px;line-height:8px;">&#8202;</div>
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            </td></tr><tr><td class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" width="600px">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" role="presentation" style="width:568px;" width="568"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="r  pr-16 pl-16" style="background:#eeeeee;background-color:#eeeeee;margin:0px auto;border-radius:4px 4px 4px 4px;max-width:568px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#eeeeee;background-color:#eeeeee;width:100%;border-radius:4px 4px 4px 4px;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="width:536px;">
            <![endif]--><div class="pc100 ogf" style="font-size:0;line-height:0;text-align:left;display:inline-block;width:100%;direction:ltr;">
            <!--[if mso | IE]>
            <table border="0" cellpadding="0" cellspacing="0" role="presentation"><tr><td style="vertical-align:middle;width:260px;">
            <![endif]--><div class="pc48-5075 ogf m c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:48.5075%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="left" class="x" style="font-size:0;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:22px;mso-ansi-font-size:18px;"><span style="font-size:17px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:124%;mso-line-height-alt:22px;mso-ansi-font-size:18px;">Amazingly delicious hand crafted sushi</span></p></div>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td style="width:16px;">
            <![endif]--><div class="pc2-9851 ogf g" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:2.9851%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td style="vertical-align:middle;width:260px;">
            <![endif]--><div class="pc48-5075 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:48.5075%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="right" class="i" style="font-size:0;padding:0;word-break:break-word;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0;"><tbody><tr><td style="width:44px;"> <img alt src="img/e46a6d60b80e2794caf3b449151c2489.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" title width="44" height="auto">
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]--></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            </td></tr><tr><td class="" width="600px">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:568px;" width="568"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div style="margin:0px auto;max-width:568px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;"><tbody><tr><td style="direction:ltr;font-size:0;padding:0;text-align:center;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="width:568px;">
            <![endif]--><div class="pc100 ogf" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody><tr><td class="s" style="font-size:0;padding:0;word-break:break-word;" aria-hidden="true"><div style="height:8px;line-height:8px;">&#8202;</div>
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            </td></tr><tr><td class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" width="600px">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" role="presentation" style="width:568px;" width="568"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="r  pr-16 pl-16" style="background:#eeeeee;background-color:#eeeeee;margin:0px auto;border-radius:4px 4px 4px 4px;max-width:568px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#eeeeee;background-color:#eeeeee;width:100%;border-radius:4px 4px 4px 4px;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="width:536px;">
            <![endif]--><div class="pc100 ogf" style="font-size:0;line-height:0;text-align:left;display:inline-block;width:100%;direction:ltr;">
            <!--[if mso | IE]>
            <table border="0" cellpadding="0" cellspacing="0" role="presentation"><tr><td style="vertical-align:middle;width:260px;">
            <![endif]--><div class="pc48-5075 ogf m c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:48.5075%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="left" class="x" style="font-size:0;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:22px;mso-ansi-font-size:18px;"><span style="font-size:17px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:124%;mso-line-height-alt:22px;mso-ansi-font-size:18px;">Amazingly delicious hand crafted sushi</span></p></div>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td style="width:16px;">
            <![endif]--><div class="pc2-9851 ogf g" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:2.9851%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td style="vertical-align:middle;width:260px;">
            <![endif]--><div class="pc48-5075 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:48.5075%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="right" class="i" style="font-size:0;padding:0;word-break:break-word;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0;"><tbody><tr><td style="width:44px;"> <img alt src="img/e46a6d60b80e2794caf3b449151c2489.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" title width="44" height="auto">
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]--></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            </td></tr><tr><td class="" width="600px">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="" role="presentation" style="width:568px;" width="568"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div style="margin:0px auto;max-width:568px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;"><tbody><tr><td style="direction:ltr;font-size:0;padding:0;text-align:center;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="width:568px;">
            <![endif]--><div class="pc100 ogf" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody><tr><td class="s" style="font-size:0;padding:0;word-break:break-word;" aria-hidden="true"><div style="height:8px;line-height:8px;">&#8202;</div>
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            </td></tr><tr><td class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" width="600px">
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" role="presentation" style="width:568px;" width="568"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="r  pr-16 pl-16" style="background:#eeeeee;background-color:#eeeeee;margin:0px auto;border-radius:4px 4px 4px 4px;max-width:568px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#eeeeee;background-color:#eeeeee;width:100%;border-radius:4px 4px 4px 4px;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:16px 16px 16px 16px;text-align:left;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="width:536px;">
            <![endif]--><div class="pc100 ogf" style="font-size:0;line-height:0;text-align:left;display:inline-block;width:100%;direction:ltr;">
            <!--[if mso | IE]>
            <table border="0" cellpadding="0" cellspacing="0" role="presentation"><tr><td style="vertical-align:middle;width:260px;">
            <![endif]--><div class="pc48-5075 ogf m c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:48.5075%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="left" class="x" style="font-size:0;word-break:break-word;"><div style="text-align:left;"><p style="Margin:0;text-align:left;mso-line-height-alt:22px;mso-ansi-font-size:18px;"><span style="font-size:17px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:124%;mso-line-height-alt:22px;mso-ansi-font-size:18px;">Amazingly delicious hand crafted sushi</span></p></div>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td style="width:16px;">
            <![endif]--><div class="pc2-9851 ogf g" style="font-size:0;text-align:left;direction:ltr;display:inline-block;width:2.9851%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%"><tbody><tr><td style="padding:0;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%"><tbody></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td><td style="vertical-align:middle;width:260px;">
            <![endif]--><div class="pc48-5075 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:48.5075%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="right" class="i" style="font-size:0;padding:0;word-break:break-word;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0;"><tbody><tr><td style="width:44px;"> <img alt src="img/e46a6d60b80e2794caf3b449151c2489.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" title width="44" height="auto">
            </td></tr></tbody></table>
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]--></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            </td></tr></table>
            <![endif]-->
            </td></tr></tbody></table></div>
            <!--[if mso | IE]>
            </td></tr></table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" class="r-outlook -outlook pr-16-outlook pl-16-outlook -outlook" role="presentation" style="width:600px;" width="600"><tr><td style="line-height:0;font-size:0;mso-line-height-rule:exactly;">
            <![endif]--><div class="r  pr-16 pl-16" style="background:#fffffe;background-color:#fffffe;margin:0px auto;max-width:600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#fffffe;background-color:#fffffe;width:100%;"><tbody><tr><td style="border:none;direction:ltr;font-size:0;padding:24px 16px 24px 16px;text-align:left;">
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="c-outlook -outlook -outlook" style="vertical-align:middle;width:568px;">
            <![endif]--><div class="xc568 ogf c" style="font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border:none;vertical-align:middle;" width="100%"><tbody><tr><td align="center" class="i  m" style="font-size:0;padding:0;padding-bottom:16px;word-break:break-word;">
            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0;"><tbody><tr><td style="width:74px;"> <img alt src="img/b9f9c19429a7af8b64e6f374f5594103.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" title width="74" height="auto">
            </td></tr></tbody></table>
            </td></tr><tr><td align="center" class="v  s-8" style="font-size:0;padding-bottom:0;word-break:break-word;"><div class="il" style>
            <!--[if mso | IE]>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center"><tr><td style="padding:0;padding-top:0;padding-left:0;padding-right:8px;padding-bottom:0;" class="l-outlook -outlook m-outlook">
            <![endif]--> <a class="l  m" href="#insertUrlLink" target="_blank" style="display:inline-block;color:#000000;font-family:'Inter',Arial,sans-serif;font-size:13px;font-weight:normal;line-height:0;text-decoration:none;text-transform:none;padding:0;padding-top:0;padding-left:0;padding-right:8px;padding-bottom:0;"> <span style="font-size:13px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:123%;text-decoration:underline;mso-line-height-alt:16px;mso-ansi-font-size:14px;">Sushi
            Menu</span></a>
            <!--[if mso | IE]>
            </td><td style="padding:0;padding-top:0;padding-left:0;padding-right:8px;padding-bottom:0;" class="l-outlook -outlook m-outlook">
            <![endif]—> <a class="l  m" href="#insertUrlLink" target="_blank" style="display:inline-block;color:#000000;font-family:'Inter',Arial,sans-serif;font-size:13px;font-weight:normal;line-height:0;text-decoration:none;text-transform:none;padding:0;padding-top:0;padding-left:0;padding-right:8px;padding-bottom:0;"> <span style="font-size:13px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:123%;text-decoration:underline;mso-line-height-alt:16px;mso-ansi-font-size:14px;">Download
            App</span></a>
            <!—[if mso | IE]>
            </td><td style="padding:0;padding-top:0;padding-left:0;padding-right:0;padding-bottom:0;" class="l-outlook -outlook -outlook">
            <![endif]—> <a class="l  " href="#insertUrlLink" target="_blank" style="display:inline-block;color:#000000;font-family:'Inter',Arial,sans-serif;font-size:13px;font-weight:normal;line-height:0;text-decoration:none;text-transform:none;padding:0;padding-top:0;padding-left:0;padding-right:0;padding-bottom:0;"> <span style="font-size:13px;font-family:'Inter',Arial,sans-serif;font-weight:700;color:#000000;line-height:123%;text-decoration:underline;mso-line-height-alt:16px;mso-ansi-font-size:14px;">Book
            Now</span></a>
            <!—[if mso | IE]>
            </td></tr></table>
            <![endif]—></div>
            </td></tr></tbody></table></div>
            <!—[if mso | IE]>
            </td></tr></table>
            <![endif]—>
            </td></tr></tbody></table></div>
            <!—[if mso | IE]>
            </td></tr></table>
            <![endif]—></div>
            </body>
        </html>
        """
    content_part = MIMEText(html_body, "html")
    msg.attach(content_part)
    

    send_email(to_mail)
    
    smtp.quit()