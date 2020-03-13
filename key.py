import os

def xfz():
    os.system("clear")
    print("[ Tools Special keys for termux ]\n{ Author : Renz Rafael }\n")
    print("[*] Getting Termux Properties...")
    try:
        os.mkdir("/data/data/com.termux/files/home/.termux")
    except OSError:
        pass
    kf = open("/data/data/com.termux/files/home/.termux/termux.properties", "w")
    kf.write("extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]")
    kf.close()
    os.system("termux-reload-settings")
    print("\n[*] Please Restart Termux!\n[+] All Done")
     
xfz()