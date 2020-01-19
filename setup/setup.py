import os

# os.system('')

if __name__ == '__main__':
    flag = False
    print('......设置镜像源......')
    os.system('sudo chmod o+w /etc/pacman.conf')
    with open('/etc/pacman.conf', 'r') as f:
        lin = f.readline()
        while lin:
            if lin == '[archlinuxcn]\n' \
                    and f.readline() == 'Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch\n':
                print('文件 /etc/pacman.conf 无需配置')
                flag = True
                break
            lin = f.readline()
    with open('/etc/pacman.conf', 'a+') as f:
        if flag:
            flag = False
        else:
            f.write('[archlinuxcn]\nServer = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch\n')
            print('文件 /etc/pacman.conf 配置成功')
    os.system('sudo chmod o-w /etc/pacman.conf')

    print('......更新镜像源......')
    os.system('echo y |sudo pacman -Sy archlinuxcn-keyring')

    print('......安装PIP......')
    os.system('sudo pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package')
    os.system('sudo pip install pip -U')
    os.system('sudo pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple')

    print('......安装\卸载软件......')
    os.system('echo y |sudo pacman -S fish')
    os.system('chsh -s /usr/bin/fish')
    os.system('curl -L https://get.oh-my.fish | fish')

    os.system('sudo pacman -S fcitx-im fcitx-sogoupinyin fcitx-configtool wine_gecko wine-mono winetricks-zh wine jdk8  netease-cloud-music gimp firefox firefox-i18n-zh-cn wps-office cmake make gcc gdb visual-studio-code-bin clion deepin.com.qq.im gnome-terminal-fedora exfat-utils  dsniff net-tools advcp deepin-system-monitor deepin-music deepin-editor deepin-movie d flashplugin deepin-movie virtualbox virtualbox-guest-utils virtualbox-guest-iso linux419-virtualbox-host-modules')
    os.system('yay -S deepin.com.thunderspeed')
    os.system('sudo /sbin/rcvboxdrv setup ')

    print('......配置输入法......')
    os.system('sudo chmod o+w /etc/profile')
    with open('/etc/profile', 'r') as f:
        lin = f.readline()
        while lin:
            if lin == 'export GTK2_RC_FILES="$HOME/.gtkrc-2.0"\n' \
                    and f.readline() == 'export LC_CTYPE=zh_CN.UTF-8\n' \
                    and f.readline() == 'export XMODIFIERS=@im=fcitx\n' \
                    and f.readline() == 'export GTK_IM_MODULE=fcitx\n' \
                    and f.readline() == 'export QT_IM_MODULE=fcitx\n':
                print('输入法无需配置')
                flag = True
                break
            lin = f.readline()
    with open('/etc/profile', 'a+') as f:
        if flag:
            flag = False
        else:
            f.write(
                'export GTK2_RC_FILES="$HOME/.gtkrc-2.0"\nexport LC_CTYPE=zh_CN.UTF-8\nexport XMODIFIERS=@im=fcitx\nexport GTK_IM_MODULE=fcitx\nexport QT_IM_MODULE=fcitx\n')
            print('输入法配置成功')
    os.system('sudo chmod o-w /etc/profile')

    print('......完成......')
