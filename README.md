## Инструкция по установке проекта на сервер Amazon EC2

#

1. Запустить инстанс VPC с ОС Ubuntu 20. (версия Python3.8 предустановлена)
2. $ sudo apt update # обновить компоненты

#

3. cd /home # перейти в папку /home
4. $ python3.8 -m pip install --upgrade pip # установить pip
5. $ pip install virtualenv # скачать пакет виртуального окружения
6. $ git clone /project/...# перенести папку проекта с github
7. $ cd project # перейти в папку проекта
8. $ virtualenv venv
9. $ source venv/bin/activate
   $ deactivate

# установка сервера redis

$ sudo apt install redis-server
$ redis-cli
127.0.0.1:6379> ping
ответ PONG
Переменные окружения. Теперь нужно спрятать токен и API-ключ в переменные. Выполните команду
$ sudo nano /etc/environment
и вставьте эти строки со своими значениями в кавычках.
token="замените*на*токен"

...

cd /home/project/ # перейдем в папку проекта
$ source venv/bin/activate # активируем окружение
поменять настройки доступа к папке виртуального окружения
$ sudo chmod ugo+rwx /home/project/venv/lib/python3.8/site-packages/
$ pip3 install -r requirements.txt # установим зависимости
$ python project.py # запустим проект
Теперь перейдите в Телеграм и протестируйте работу. Отвечает? Хорошо, остановите его (ctrl+c) и деактивируйте виртуальное окружение (deactivate)
...
Создадим собственную службу для постоянной работы бота и перезапуска в случае падения.

### nano /lib/systemd/system/project.service

- Текст скрипта project.service:

[Unit]
Description=online bot

After=network.target

[Service]

EnvironmentFile=/etc/environment
ExecStart=/home/project/venv/bin/python3 main.py
ExecReload=/home/project/venv/bin/python3 main.py
WorkingDirectory=/home/project/
KillMode=process
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target

### CTRL+O -> Enter -> CTRL+X для сохранения.

### Настройки службы:

Description — описание службы.

EnvironmentFile — путь к файлу с переменными.

ExecStart и ExecReload — это команды для запуска и перезапуска бота.

WorkingDirectory — путь к папке в которой файл запуска main.py.

### Для запуска службы выполните эти 2 команды.

- $ systemctl enable project
- $ systemctl start project

$ sudo systemctl status project # статус

$ journalctl -u project.service # логи
