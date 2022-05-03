import ftplib
import optparse
def anon_login(hostname):
    try:

        ftp = ftplib.FTP(hostname)
        ftp.login("anonymous")
        print("\n [+]" + str(hostname) + "FTP Anonymous login succeded")
        ftp.quit()
        return True

    except:
        print("\n [+]" + str(hostname) + "FTP Anonymous login Failed")
        return False
def getting_input():
    object_parse = optparse.OptionParser()
    object_parse.add_option("-i", "--ip", dest="ip", help="ip to change")
    return object_parse.parse_args()

[user_input,arguements] = getting_input()  

if __name__ == "__main__":
   anon_login(user_input.ip)
