import os,e32,appuifw,sysinfo,miso,appswitch

appuifw.app.screen='normal'
def ru(x):return x.decode('utf-8')
appuifw.app.title=u'HY Mobile'
txt = appuifw.Text()
appuifw.app.body = txt
appuifw.app.body.color = (0,0,0)
prgpath="E:\\System\\Apps\\HY\\"
def kaydet():
    CONFIG_DIR='E:/System/Apps/HY'
    CONFIG_FILE=os.path.join(CONFIG_DIR,'mysettings.txt')
    if not os.path.isdir(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
        CONFIG_FILE=os.path.join(CONFIG_DIR,'mysettings.txt')      
    config={}
    config['variable1']= prgdili
    f=open(CONFIG_FILE,'wt')
    f.write(repr(config))
    f.close()
    oku()
def oku():
    CONFIG_FILE='E:/System/Apps/HY/mysettings.txt'
    try:
        f=open(CONFIG_FILE,'rt')
        try:
            content = f.read()
            config=eval(content)
            f.close()
            global prgdili
            prgdili=config.get('variable1','')
        except:
            print 'dosya okunamiyor'
    except:
        print 'dosya acilamiyor'
        
class FileSelector:
    def __init__(self,dir=".",ext='.jpg'):
        self.dir = dir
        self.ext = ext
        self.files = {}
 
        def iter(fileselector,dir,files):
            for file in files:
                b,e = os.path.splitext(file)
                if e == fileselector.ext:
                    fileselector.files[u'%s' % b] = os.path.join(dir,file)
 
        try:
            os.path.walk(self.dir,iter,self)
        
        except:
            pass
        self.sortedkeys = self.files.keys()
        self.sortedkeys.sort()
 
    def GetKeys(self):
        return self.sortedkeys
 
    def GetFile(self,index):
        return self.files[self.sortedkeys[index]]
def dilsec():
    appuifw.note(ru("Please select your language"), 'conf')
    selector = FileSelector("e:\\System\\Apps\\HY\\langs",".lang")
    index = appuifw.selection_list(selector.GetKeys())
    if index is not None:
        appuifw.note(u"File %s selected." % selector.GetFile(index), "info")
        global prgdili
        prgdili=selector.GetFile(index)
    else:
        appuifw.note(u"No file selected.", "info")
        global prgdili
        prgdili='0'
    kaydet()    
    dil() 

def dil(): 
    oku()
    if prgdili=='0':
        dilsec()
    else:
        try:
            f=file(prgdili,'rb')
            global language
            language=f.read().split('\n')
            f.close()
        except:
            appuifw.note(ru('Language file is damaged.'),'error')
            dilsec()        
            
dil()


def lang(string):
    return language[string-1]
def anabilgiler():    
    eyer= sysinfo.free_drivespace()['E:'] 
    global eyer3
    eyer3=eyer/1024
    global eyer4
    eyer4 = eyer3
    global oncekiyere
    oncekiyere = unicode(eyer4)
    rama=sysinfo.free_ram()
    ramb=rama/1024
    global rambos
    rambos=unicode(ramb)
    cyer= sysinfo.free_drivespace()['C:'] 
    global cyer3
    cyer3=cyer/1024
    global cyer4
    cyer4 = cyer3
    global oncekiyerc
    oncekiyerc = unicode(cyer4)

kb=ru("KB")
satir=ru("\n")

def anaekran():
    anabilgiler()
    txt.set(ru(lang(1))+satir+ru(lang(2))+satir+ru(lang(3))+satir+satir+ru(lang(4))+oncekiyerc+kb+satir+ru(lang(5))+oncekiyere+kb+satir+ru(lang(6))+rambos+kb)
    
anaekran()
rebuild=1

def yardim():
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "file://e:/system/apps/HY/help.html"')
def hakkinda():
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "file://e:/system/apps/HY/hakkinda.html"')
def ilktik():
    e32.start_exe('z:\\system\\programs\\apprun.exe','z:\\system\\apps\\browser\\browser.app "http://www.ilktik.com/wap/index.php"')
def guncelle():
    e32.start_exe('z:\\system\\programs\\apprun.exe','E:\\System\\Apps\\HY\\Guncelleme\\Guncelleme.app')
    e32.ao_sleep(1)
    e32.start_exe('z:\\system\\programs\\apprun.exe','E:\\System\\Apps\\HY\\Guncelleme\\Guncelleme.app')

def temizle():
    global rebuild
    rebuild=0
    txt.set(ru(lang(7)))
    e32.ao_sleep(8)
    restart()
def restart():

    if (appuifw.query(ru(lang(8)), 'query') == True):
         appuifw.note(ru(lang(9)))
         temc()
    else:
         appuifw.note(ru(lang(32)), 'info')
         anaekran()
         global rebuild
         rebuild=1

index=0


def del_dir(path):
   for name in os.listdir(path):
      e32.ao_sleep(0.001)
      new=path+'\\'+name
      if os.path.isdir(new):
         del_dir(new)
         try:
            os.rmdir(new)
         except:
            pass
      else:
         try:
            os.remove(new)
         except:
            pass

            

def dirmm(path):
   global index
   for name in os.listdir(path):
      e32.ao_sleep(0.001)
      new=path+'\\'+name
      if os.path.isdir(new):
         if new.endswith('_PAlbTN'):
            del_dir(new)
            try:
               os.rmdir(new)
            except:
               pass
            else:
               index+=1
         else:
            dirmm(new)



def dbdel(path):
   global index
   for name in os.listdir(path):
      e32.ao_sleep(0.001)
      new=path+'\\'+name
      if os.path.isdir(new):
            dbdel(new)
      else:
            if new.endswith('thumbs.db'):
                os.remove(new)



def hazirlan():
    asama="1/6"
    txt.set(ru(lang(10))+satir+ru(lang(11))+bosluk+asama+satir+ru(lang(12))) 
    e32.ao_sleep(6)
    try:
         appswitch.end_app(u"Galeri")
    except:
         pass
#dosya
    try:
         appswitch.end_app(u"Kamera")
    except:
         pass

#dosya
    try:
         appswitch.end_app(u"Müzik çalar")
    except:
         pass

#dosya
    try:
         appswitch.end_app(u"Music player")
    except:
         pass

#dosya
    try:
         appswitch.end_app(u"Movie director")
    except:
         pass

#dosya
    try:
         appswitch.end_app(u"Gallery")
    except:
         pass


#dosya
    try:
         appswitch.end_app(u"Camera")
    except:
         pass


#dosya
    try:
         appswitch.end_app(u"Dosy. yöneticisi")
    except:
         pass

#dosya
    try:
         appswitch.end_app(u"File manager")
    except:
         pass


#dosya
    try:
         appswitch.end_app(u"RealPlayer")
    except:
         pass


#dosya
    try:
         appswitch.end_app(u"FExplorer")
    except:
         pass


#dosya
    try:
         appswitch.end_app(u"Web")
    except:
         pass

#dosya
    try:
         appswitch.end_app(u"X-plore")
    except:
         pass


#dosya
    try:
         appswitch.end_app(u"Fileman")
    except:
         pass
    temc()


def temc(): 
    asama="2/6"
    txt.set(ru(lang(13))+satir+ru(lang(11))+bosluk+asama+satir+ru(lang(14)))
    e32.ao_sleep(5)


#yeni
    try:
         del_dir("c:\\cache")
    except:
         pass
    try:
         os.rmdir("c:\\cache")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\trm")
    except:
         pass
    try:
         os.rmdir("c:\\trm")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\System\\Apps\\bindpa")
    except:
         pass
    try:
         os.rmdir("c:\\System\\Apps\\bindpa")
    except:
         pass
    try:
         os.rmdir("c:\\System\\Apps\\BINDPA")
    except:
         pass

    try:
         os.rmdir("c:\\System\\Apps\\BiNDPA")
    except:
         pass
         
         #yeni
    try:
         del_dir("c:\\System\\Apps\\appinst")
    except:
         pass
    try:
         os.rmdir("c:\\System\\Apps\\appinst")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\system\\mtm")
    except:
         pass
    try:
         os.rmdir("c:\\system\\mtm")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\modul")
    except:
         pass
    try:
         os.rmdir("c:\\modul")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\ezfilemon")
    except:
         pass
    try:
         os.rmdir("c:\\ezfilemon")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\photosafe")
    except:
         pass
    try:
         os.rmdir("c:\\photosafe")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\powermp3")
    except:
         pass
    try:
         os.rmdir("c:\\powermp3")
    except:
         pass
         
         #yeni
    try:
         del_dir("c:\\ezfilemon")
    except:
         pass
    try:
         os.rmdir("c:\\ezfilemon")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\System\\Apps\\zeonantivirus")
    except:
         pass
    try:
         os.rmdir("c:\\System\\Apps\\zeonantivirus")
    except:
         pass
         #yeni
    try:
         del_dir("c:\\system\\data\\ahle\\ahleurl")
    except:
         pass
    try:
         os.rmdir("c:\\system\\data\\ahle\\ahleurl")
    except:
         pass
         
         #yeni
    try:
         del_dir("c:\\system\\data\\ahle\\mobiolaplayer")
    except:
         pass
    try:
         os.rmdir("c:\\system\\data\\ahle\\mobiolaplayer")
    except:
         pass
         
         #yeni
    try:
         del_dir("c:\\system\\data\\ahle\\powermp3")
    except:
         pass
    try:
         os.rmdir("c:\\system\\data\\ahle\\powermp3")
    except:
         pass
    teme()
    
def teme():
    asama="3/6"
    txt.set(ru(lang(13))+satir+ru(lang(11))+bosluk+asama+satir+ru(lang(15)))
    e32.ao_sleep(5)

#yeni
    try:
         del_dir("E:\\trm")
    except:
         pass
    try:
         os.rmdir("E:\\trm")
    except:
         pass
#yeni
    try:
         del_dir("E:\\System\\Apps\\appinst")
    except:
         pass
    try:
         os.rmdir("E:\\System\\Apps\\appinst")
    except:
         pass
#yeni
    try:
         del_dir("E:\\System\\Apps\\bindpa")
    except:
         pass
    try:
         os.rmdir("E:\\System\\Apps\\bindpa")
    except:
         pass
#yeni
    try:
         del_dir("E:\\cache")
    except:
         pass
    try:
         os.rmdir("E:\\cache")
    except:
         pass
#yeni
    try:
         del_dir("E:\\System\\Apps\\muvee")
    except:
         pass
    try:
         os.rmdir("E:\\System\\Apps\\muvee")
    except:
         pass
#yeni
    try:
         del_dir("E:\\system\\libs\\ncuibrowser")
    except:
         pass
    try:
         os.rmdir("E:\\system\\libs\\ncuibrowser")
    except:
         pass
#yeni
    try:
         del_dir("E:\\system\\temp")
    except:
         pass
    try:
         os.rmdir("E:\\system\\temp")
    except:
         pass
#yeni
    try:
         del_dir("E:\\system\\data\\opera\\cache4")
    except:
         pass
    try:
         os.rmdir("E:\\system\\data\\opera\\cache4")
    except:
         pass
    temfiles()
    
def temfiles():
    asama="4/6"
    txt.set(ru(lang(13))+satir+ru(lang(11))+bosluk+asama+satir+ru(lang(16)))
    dbdel("e:")
    dbdel("c:")
    try:
        os.remove('E:\\install.log')
    except:
        pass
#dosya
    try:
        os.remove('E:\\system\\temp.jpg')
    except:
        pass

#dosya
    try:
        os.remove('c:\\install.log')
    except:
        pass
#dosya
    try:
        os.remove('c:\\instapp.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\fileslst.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\phyton_error.log')
    except:
        pass

#dosya
    try:
        os.remove('E:\\phyton_error')
    except:
        pass
#dosya
    try:
        os.remove('E:\\phyton_error.log')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\data\\ahle\\ahleurl')
    except:
        pass


#dosya
    try:
        os.remove('c:\\system\\data\\bt00010217.dat')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\data\\devlist.dat')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\data\\fep.ini')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\data\\music.db')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\install\\install.log')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\mtm\\mtm registry v2')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\install\\install.log')
    except:
        pass
#dosya
    try:
        os.remove('E:\\system\\libs\\ecom.dll')
    except:
        pass
#dosya
    try:
        os.remove('E:\\system\\libs\\ecomserver.exe')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\libs\\http.dll')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\libs\\httptcphnd.dll')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\libs\\inetprotutil.dll')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\libs\\loaderclings.dll')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\libs\\loadersvngs.exe')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\libs\\ncuiutil.dll')
    except:
        pass


#dosya
    try:
        os.remove('E:\\system\\libs\\plugins\\backlightctrl.dll')
    except:
        pass
#dosya
    try:
        os.remove('E:\\python_error.log')
    except:
        pass
#dosya
    try:
        os.remove('c:\\python_error.log')
    except:
        pass

        
#dosya
    try:
        os.remove('E:\\system\\libs\\plugins\\tfcorefilters.dll')
    except:
        pass



#dosya
    try:
        os.remove('E:\\system\\libs\\rbinterpretengs.dll')
    except:
        pass


#dosya
    try:
        os.remove('E:\\system\\libs\\securesocket.dll')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\libs\\ssl70.dll')
    except:
        pass


#dosya
    try:
        os.remove('E:\\system\\libs\\ssladaptor.dll')
    except:
        pass


#dosya
    try:
        os.remove('E:\\system\\libs\\tfcorefilters.dll')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\libs\\rbinterpretengs.dll')
    except:
        pass
#dosya
    try:
        os.remove('c:\\system\\libs\\ecom.dll')
    except:
        pass
#dosya
    try:
        os.remove('c:\\system\\libs\\ecomserver.exe')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\libs\\http.dll')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\libs\\httptcphnd.dll')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\libs\\inetprotutil.dll')
    except:
        pass
#dosya
    try:
        os.remove('c:\\System\\Apps\\CorePlayer\\library.db')
    except:
        pass
#dosya        
    try:
        os.remove('E:\\System\\Apps\\CorePlayer\\library.db')
    except:
        pass
#dosya
    try:
        os.remove('c:\\system\\libs\\loaderclings.dll')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\libs\\loadersvngs.exe')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\libs\\ncuiutil.dll')
    except:
        pass


#dosya
    try:
        os.remove('c:\\system\\libs\\plugins\\backlightctrl.dll')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\libs\\plugins\\tfcorefilters.dll')
    except:
        pass



#dosya
    try:
        os.remove('c:\\system\\libs\\rbinterpretengs.dll')
    except:
        pass


#dosya
    try:
        os.remove('c:\\system\\libs\\securesocket.dll')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\libs\\ssl70.dll')
    except:
        pass


#dosya
    try:
        os.remove('c:\\system\\libs\\ssladaptor.dll')
    except:
        pass


#dosya
    try:
        os.remove('c:\\system\\libs\\tfcorefilters.dll')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\libs\\rbinterpretengs.dll')
    except:
        pass
#dosya
    try:
        os.remove('c:\\_mp3declog.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\asphalt.log')
    except:
        pass

#dosya
    try:
        os.remove('c:\\debug.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\ezfilemon.txt')
    except:
        pass

#dosya
    try:
        os.remove('c:\\file.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\nokia\\startermonlog.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\pvp.log')
    except:
        pass
#dosya
    try:
        os.remove('c:\\sticqlog.txt.log')
    except:
        pass

#dosya
    try:
        os.remove('c:\\sw_scry_check.dat')
    except:
        pass
#dosya
    try:
        os.remove('c:\\system\\data\\bt00010217.dat')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\data\\cbruiexe.b93')
    except:
        pass


#dosya
    try:
        os.remove('c:\\system\\data\\devlist.dat')
    except:
        pass
#dosya
    try:
        os.remove('c:\\system\\data\\fep.ini')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\data\\fontrouter.txt')
    except:
        pass

#dosya
    try:
        os.remove('c:\\system\\install\\install.log')
    except:
        pass
#dosya
    try:
        os.remove('c:\\x-etalon.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\x-settings.txt')
    except:
        pass
#dosya
    try:
        os.remove('E:\\_mp3declog.txt')
    except:
        pass
#dosya
    try:
        os.remove('E:\\asphalt.log')
    except:
        pass

#dosya
    try:
        os.remove('E:\\debug.txt')
    except:
        pass
#dosya
    try:
        os.remove('E:\\ezfilemon.txt')
    except:
        pass

#dosya
    try:
        os.remove('E:\\file.txt')
    except:
        pass
#dosya
    try:
        os.remove('E:\\nokia\\startermonlog.txt')
    except:
        pass
#dosya
    try:
        os.remove('E:\\pvp.log')
    except:
        pass
#dosya
    try:
        os.remove('E:\\sticqlog.txt.log')
    except:
        pass

#dosya
    try:
        os.remove('E:\\sw_scry_check.dat')
    except:
        pass
#dosya
    try:
        os.remove('E:\\system\\data\\bt00010217.dat')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\data\\cbruiexe.b93')
    except:
        pass


#dosya
    try:
        os.remove('E:\\system\\data\\devlist.dat')
    except:
        pass
#dosya
    try:
        os.remove('E:\\system\\data\\fep.ini')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\data\\fontrouter.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\system\\temp.jpg')
    except:
        pass

    try:
        os.remove('E:\\system\\temp.jpg')
    except:
        pass

#dosya
    try:
        os.remove('E:\\system\\install\\install.log')
    except:
        pass
#dosya
    try:
        os.remove('E:\\x-etalon.txt')
    except:
        pass
#dosya
    try:
        os.remove('E:\\x-settings.txt')
    except:
        pass

#dosya
    try:
        os.remove('E:\\linetx.exe')
    except:
        pass
#dosya
    try:
        os.remove('E:\\nito.exe')
    except:
        pass
#dosya
    try:
        os.remove('E:\\nokia\\installs\\tmp87bf1.$$$')
    except:
        pass

#dosya
    try:
        os.remove('E:\\skaner\\log\\data\\log.txt')
    except:
        pass
#dosya
    try:
        os.remove('E:\\System\\Apps\\exe\\your.exe')
    except:
        pass
#dosya
    try:
        os.remove('E:\\System\\Apps\\exe\\your.exe')
    except:
        pass
#dosya
    try:
        os.remove('c:\\linetx.exe')
    except:
        pass
#dosya
    try:
        os.remove('c:\\nito.exe')
    except:
        pass
#dosya
    try:
        os.remove('c:\\nokia\\installs\\tmp87bf1.$$$')
    except:
        pass

#dosya
    try:
        os.remove('c:\\skaner\\log\\data\\log.txt')
    except:
        pass
#dosya
    try:
        os.remove('c:\\System\\Apps\\exe\\your.exe')
    except:
        pass
#dosya
    try:
        os.remove('c:\\System\\Apps\\exe\\your.exe')
    except:
        pass
#dosya
    try:
        os.remove('c:\\System\\Apps\\ksmobile\\kavlogs.klf')
    except:
        pass
        
        temimg()
def tamam():
    asama="6/6"
    eyerk=sysinfo.free_drivespace()['E:'] 
    eyerk3=eyerk/1024
    cyerk=sysinfo.free_drivespace()['C:'] 
    cyerk3=cyerk/1024
    kazanilanc1=cyer4-cyerk3
    kazanilanc3=unicode(kazanilanc1)
    kazanilane1=eyer4-eyerk3
    kazanilane3=unicode(kazanilane1)

    text2=ru("HY Mobile 2.0\nTemizleme Tamamlandı!\nAşama 6/6:\nTemizleme Tamamlandı...\n Telefon Hafızasından")
    text3=ru("Hafıza Kartından")
    text4=ru("Yer Kazanıldı")
    txt.set(ru(lang(19))+satir+ru(lang(11))+bosluk+asama+satir+ru(lang(20))+bosluk+kazanilanc3+kb+satir+ru(lang(21))+bosluk+kazanilane3+kb+satir+ru(lang(22)))
    e32.ao_sleep(8)
    anabilgiler()
    anaekran()
    global rebuild
    rebuild=1
        
def temimg():
    if (appuifw.query(ru(lang(31)), 'query') == True):
        asama="5/6"
        txt.set(ru(lang(13))+satir+ru(lang(11))+bosluk+asama+satir+ru(lang(17))+satir+ru(lang(18)))
        dirmm('c:')
        e32.ao_yield()
        dirmm('e:')
    tamam()

bosluk=" "



def cram():
    r=sysinfo.free_ram()
    r1=str(r)
    r2=int(r1)
    if (appuifw.query(ru(lang(34)), 'query') == True):
         closer()
    try:
         miso.compress_all_heaps()
         miso.compress_all_heaps()
         r3=sysinfo.free_ram()
         r4=str(r3)
         r5=int(r4)
         r6=(r5-r2)/1024
         rbos=r5/1024
         bos=str(rbos) 
         r7=str(r6)
         appuifw.note(ru(lang(23))+satir+r7+kb+ru(lang(22))+bos+kb+ru(lang(24)))
    except:
         appuifw.note(u"Error!")
    anabilgiler()
    anaekran() 
         

def closer():
    apps = appswitch.application_list(True) # true = include all
       # false = no hidden apps 

    for app in apps:
        if app=="Telefon":
            gec=1
        elif app=="Phone":
            gec=1   
        elif app=="HY":
            gec=1     
        elif app=="Python":
            gec=1
        elif app=="anykey":
            gec=1          
        elif app=="SysAp":
            gec=1         
        elif app=="Autolock":
            gec=1        
        elif app=="EiksrvBackdrop":
            gec=1         
        else:
            appswitch.kill_app(app)  

        appswitch.switch_to_fg(u"Python")
    appuifw.note(ru(lang(35)))
    anabilgiler()
    anaekran()
        
        
appuifw.app.menu = [
 (ru(lang(25)),temizle),
 (ru(lang(26)),cram),
 (ru(lang(33)),closer),
 (ru("Language"),dilsec),
 (ru(lang(27)),hakkinda),
 (ru(lang(30)),ilktik)]
 
def refresh():
    if rebuild==1:
        anaekran()
    e32.ao_sleep(2)
    refresh()
    
refresh() 


SCRIPT_LOCK = e32.Ao_lock( )
SCRIPT_LOCK.wait( )