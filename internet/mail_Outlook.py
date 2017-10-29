import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
count=0;
mails=['swaraj_somala@companyname.com','','']
for i in mails:
	print(str(count)+" "+ i)
	count = count+1;
choice = int(input('Enter mail choice'))
print("recipt is "+mails[choice])
mail = outlook.CreateItem(0)
mail_add = mails[choice]
mail.To = mail_add
#mail.To = 'swaraj_somala@avinsystems.com'
mail.Subject = 'Message subject'
mail.Body = 'Message body'
mail.HTMLBody = '<h2>HTML Message body</h2>'# this field is optional
conform = input('Enter mail choice')
#if conform == 'y':
mail.Send()
