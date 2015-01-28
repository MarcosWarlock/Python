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

for i in ext:
    for j in ext[i]:
        for k in glob.glob('/home/warlock/Desktop/' + '*.' + j):
            print (k)
            if (k[len(k)-3:len(k)]) in j:
                if not os.path.exists(j):
                    os.mkdir(j)
            shutil.copy2(k, j)
                    
        
