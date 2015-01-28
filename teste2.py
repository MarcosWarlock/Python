import glob
import os, shutil
ext = {
            'imagem':['jpg', 'jpeg', 'png', 'gif', 'bmp'],
            'musica':['mp3', 'aac', 'wav', 'flac'],
            'video':['wmv', 'mp4', 'mkv', 'rmvb', '3gp', 'avi', 'mov'],
            'script':['sh', 'py', 'java', 'bat'],
            'documento':['doc', 'docx', 'txt', 'odt'],
            'compactado':['rar', 'zip', '7zip', 'tar.gz', 'tar.gx'],
            'executavel':['exe', 'run', 'msi']
}
def Organiza(diretorio):
    if diretorio[-1] is not '/': diretorio += '/'
    for i in ext:
        for j in ext[i]:
            for k in glob.glob(diretorio + '*.' + j):
                if (k[len(k)-3:len(k)]) in j:
                    if not os.path.exists(j):
                        os.mkdir(j)
                print (str(k) + ' --> ' + str(diretorio) + str(j))
                shutil.copy2(k, j)
                    
        
