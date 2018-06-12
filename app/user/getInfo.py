from bs4 import BeautifulSoup
import requests
import sys
import iso8601


def get_info(cid,page_no):
	x=1000
	flag='success'
	stri="<html>"
	str1=""
	soln_id=[]
	date=[]
	memory=[]
	pno=[]
	pnm=[]
	lang=[]
	status=[]
	time=[]
	for i in range(1):
		r = requests.get('http://codeforces.com/submissions/'+cid+'/page/'+str(page_no))
		data = r.text
		soup = BeautifulSoup(data, "html.parser")
		if(str(soup.find('table',class_='status-frame-datatable'))==str1):
			x=i
			break
		str1=soup.find('table', class_='status-frame-datatable')
		if(str(str1)=='None'):
			flag='fail'
			break
		str2=str1.findAll('tr')
		for rows in str2:
			str3=rows.findAll('td',class_='id-cell')
			for cols in str3:
				#print(str(cols.text))
				if(cols.text!=""):
					soln_id.append(cols.text)
			str3=rows.findAll('td',class_='time-consumed-cell')
			for cols in str3:
				#print(str(cols.text))
				if(cols.text!=""):
					time.append((cols.text).replace(' ',''))
			str3=rows.findAll('td',class_='status-cell')
			for cols in str3:
				#print(str(cols.text))
				if(cols.text!=""):
					status.append((cols.text))
			str3=rows.findAll('td',class_='memory-consumed-cell')
			for cols in str3:
				#print(str(cols.text))
				if(cols.text!=""):
					memory.append((cols.text).replace(' ',''))
			str3=rows.findAll('td',class_='status-small')
			for cols in str3:
				str4=cols.findAll('a')
				for pnames in str4:
						pn=pnames.text.split()
						pno.append(pn[0])
						name=""
						for j in range(len(pn)-2):
							name+=pn[j+2]+" "
						pnm.append(name.strip())
			str3=rows.findAll('td',class_='status-small')
			j=0;
			for cols in str3:
				t=[]
				if(cols.text!=""):
					if(j%3==0):
						date.append((cols.text).replace(' ',''))
					j=j+1
					#t=cols.text.split()
					# for i in range(len(t)):
					# 	if(i%3==0):
			str3=rows.findAll('td')
			j=0;
			for cols in str3:
				#print(str(cols.text))
				if(cols.text!=""):
					if(j%4==0 and j%8!=0):
						lang.append((cols.text).replace(' ',''))
					j=j+1;
# print(memory)
	def conv(status):
		new=[]
		for k in range(len(status)):
			str1=""
			for l in range(len(status[k])):
				if(status[k][l]!='\n' and status[k][l]!='\r'):
					str1+=status[k][l]
				if(status[k][l]=='>'):
					str1+='&gt;'
				if(status[k][l]=='<'):
					str1+='&lt;'


			new.append(str1)
		return new
	status=conv(status)
	memory=conv(memory)
	date=conv(date)
	soln_id=conv(soln_id)
	pnm=conv(pnm)
	pno=conv(pno)
	lang=conv(lang)
	time=conv(time)
	arr=[]
	for j in range(len(status)):
		obj={
		'status':status[j],
		'memory':memory[j],
		'date':date[j],
		'soln_id':soln_id[j],
		'pnm':pnm[j],
		'pno':pno[j],
		"lang":lang[j],
		"time":time[j],
		"success":flag
		}
		arr.append(obj)
	if(len(status)==0):
		arr=[{'success':False}]
	return arr