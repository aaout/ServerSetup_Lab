# ServerSetpu_Lab

既にセットアップされたサーバーにユーザを追加する場合は「1. ユーザの追加」, 新しく購入したサーバーをセットアップする場合は「2. サーバーセットアップ」を参照してください. 

最終更新日: 2022/11/25 伊藤

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

    sambaとの共存のために以下のコマンドを実行してください

    ```sh
    ufw allow 22
    ufw allow Samba
    ufw app list
    ufw reload
    ```

## ソフトウェアインストール

### nvidia-driver

1. ```apt update```

2. /etc/default/grubの書き換え

    エディタを開き、以下の2項目を変更する

    > GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" -> "quiet splash pci=nomsi nomodeset"
    > 
    > GRUB_CMDLINE_LINUX="" -> "pci=noaer"

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

※ valid users = 自分のuser名

※ gest関係をnoにする

## docker run

`run.sh`にDockerのシェルスクリプトを書きました．実行したフォルダ内と同期した操作が可能になります．つまり，こちらで書き換えた内容がDockerにも同期している．実行だけDockerでできる．

`./run.sh IMAGE_NAME bash`で選択したイメージネームの環境でDockerが起動します．
こののDockerを動かすときは`./run.sh chainer5 bash`と打ちます．

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
