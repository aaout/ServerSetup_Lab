# ServerSetup_Lab

既にセットアップされたサーバーにユーザを追加する場合は「1. ユーザの追加」, 新しく購入したサーバーをセットアップする場合は「2. サーバーセットアップ」を参照してください. 

最終更新日: 2022/11/26 伊藤

![summary](/summary.png)

# 1. ユーザの追加

ユーザ名の設定

```sh
sudo adduser USERNAME
sudo pdbedit -a USERNAME
```

HDD1にディレクトリを作成. 本人以外は見られない権限に設定(chown&chmod)．

```
sudo mkdir USERNAME
sudo chown USERNAME:USERNAME USERNAME
sudo chmod 700 USERNAME
```

user追加後に対象ユーザの.bashrcに`cd /mnt/HDD1/USERNAME`を追加

smb.confを書き換える．

Dockerの権限をユーザに与える

```sh
sudo gpasswd -a ユーザ名 docker
```

# 2. サーバーセットアップ

## 引き継ぎの手順
1. サーバの移動と設置
2. OSのインストール
3. それぞれに対するPCの割り当て
4. ソフトウェアのインストール
    1. Docker
    2. Samba
    3. HDD
    4. Cron
5. VPNの設定
    1. 各ユーザを作る
    2. 自分のPCで実際にやってもらう
READMEの共有を忘れないように

## 環境構築

- フォルダ名を日本語->英語

    ※ rebootすると日本語にするか聞かれるが、チェックボックスにチェックして英語のままを選択

    ```
    LANG=C xdg-user-dirs-gtk-update
    ```

- 数字を半角入力にする設定

    ```sh
    /usr/lib/mozc/mozc_tool --mode=config_dialog
    ```
- ssh設定

    https://qiita.com/naoyukisugi/items/3602c41f143c08fadb1a

## ソフトウェアインストール

### nvidia-driver

1. ```apt update```

2. 以下のコマンドで設定ファイル開き、"GRUB_CMDLINE_LINUX_DEFAULT"と"GRUB_CMDLINE_LINUX"の項目を書き換える.

    ```sudo gedit /etc/default/grub```

    > GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
    >
    >  -> GRUB_CMDLINE_LINUX_DEFAULT="quiet splash pci=nomsi nomodeset"
    > 
    > GRUB_CMDLINE_LINUX=""
    > 
    > -> GRUB_CMDLINE_LINUX="pci=noaer"

3. 以下のコマンドを実行

    ```sh
    sudo add-apt-repository ppa:graphics-drivers/ppa
    sudo apt update
    ```

4. 推奨ドライバのインストール

    https://qiita.com/abetomo/items/a114a3c423f110460549

    1行目のコマンドを実行し、recommendされたものをインストールする

    ```sh
    ubuntu-drivers devices
    sudo apt install xxx
    ```

### nvidia-docker2

https://qiita.com/TaroNakasendo/items/44c3eecb0c1e0a91fdaf

### VSCode

以下のリンクから.deb package(64-bit)をクリックしてdebファイルをDL.

インストール後、debファイルをダブルクリックしてインストール.

https://code.visualstudio.com/docs/setup/linux

### samba
https://qiita.com/Reizouko/items/8bee9e02e74565b6c147

ファイアウォールとの共存のために以下のコマンドを実行してください

```sh
sudo ufw allow 22
sudo ufw allow Samba
sudo ufw app list
sudo ufw reload
```

※ valid users = 自分のuser名

※ gest関係をnoにする

## Add HDD

https://sicklylife.jp/ubuntu/1804/hdd_format.html

※ chmodでmntの権限を変えること

### CUI CPU application

```sh
sudo apt intall npm
sudo npm install gtop -g
gtop
```

## Backup

crontabを使います。

/etc/cron.d/の中に拡張子なしファイルを作成.

> 00 00 1 * * nishi /bin/bash /home/nishi/Desktop/backup_sh/backup1.sh
> 
> 00 00 15 * * nishi /bin/bash /home/nishi/Desktop/backup_sh/backup2.sh

backup_shには、shellscriptが入っている。

```
echo "PASSWORD" | sudo -S rm -rf /mnt/Backup1/Main1
echo "PASSWORD" | sudo -S cp -r -p /mnt/Main /mnt/Backup1
echo "PASSWORD" | sudo -S mv /mnt/Backup1/Main /mnt/Backup1/Main1
```

※ 設定後、cronを起動して設定が反映されているかを確認してください。

## devcontainer

TODO: devcontainerについての説明追加

TODO: devcontainer.jsonのアップデート
