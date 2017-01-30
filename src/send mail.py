import smtplib
from email.mime.text import MIMEText


#############

mailto_list=["name@company.com.cn"]


#####################
#设置服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.126.com"
mail_user="user"
mail_pass="password"
mail_postfix="126.com"

######################
def send_mail(to_list,sub,content):

    
    me = mail_user + "<"+mail_user + "@" + mail_postfix+">"
    
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print (e)
        return False
        
if __name__ == '__main__':
    
    if send_mail (mailto_list,"标题","内容"):
        print ("sucess")
    else:
        print ("failure")