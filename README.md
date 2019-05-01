### Facebook friend list via selenium

Application use your facebook login information to get friend list usernames and profile links

#### Application steps:
* Open web browser
* Loging to Facebook with login and password in settings
* Navigate to your profile page
* Navigate to friend list page
* Load all friend list
* Extract friend list names and profile links
* Count total friend list size ane extracted list
* Report extracted friend list

### Requirements
- Python 3.7
- Google Chrome
- Chromedriver

##### Install Chromedriver
    
```bash
$ wget https://chromedriver.storage.googleapis.com/73.0.3683.86/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip

$ sudo mv chromedriver /usr/bin/chromedriver
$ sudo chown root:root /usr/bin/chromedriver
$ sudo chmod +x /usr/bin/chromedrive
```

You can install Chromedriver with a different version, but this version must be compatible with the version of installed Google Chrome 

More Chromedriver versions: https://sites.google.com/a/chromium.org/chromedriver/downloads

#### Install additional python requirements:
   
```bash
$ python -m pip install -r ./requirements.txt
```

### Configurate application running
For run application you must set configurations. Configuration files must be in folder `Resources` with name `settings.ini

List of parameters:

* driver_path - path to chromedriver executable file
* facebook_login - facebook login (email or phone number)
* facebook_password - facebook password
* browser_headless -  run application in background without drawing UI 
* wait_time_value_in_seconds - maximum time delay web-element loading  
logging_configurations_file_path - path to file with logger settings


### Launch

```bash
$ python ./Launcher.py
```

### Execution example

```bash
$ python ./Launcher.py

2019-05-01 20:28:00,464 - INFO - Program started
2019-05-01 20:28:00,464 - INFO - Started load configuration
2019-05-01 20:28:00,464 - INFO - Start execution loading configs function
2019-05-01 20:28:00,464 - INFO - Start execution reading config file by path ./Resources/settings.ini
2019-05-01 20:28:00,464 - INFO - Data from file ./Resources/settings.ini loaded to configparser
2019-05-01 20:28:00,464 - INFO - Start writing data to configuration object
2019-05-01 20:28:00,465 - INFO - Writing data to configuration object  successfully finished
2019-05-01 20:28:00,465 - INFO - Start execution function of configuration logger
2019-05-01 20:28:00,465 - INFO - Execution function of configuration logger finished
2019-05-01 20:28:00,465 - INFO - Loading configuration finished
2019-05-01 20:28:00,465 - INFO - [SeleniumCrawler] SeleniumCrawler init
2019-05-01 20:28:01,905 - INFO - [SeleniumCrawler] Driver initiated
2019-05-01 20:28:01,905 - INFO - [SeleniumCrawler] Opening https://www.facebook.com/ page
2019-05-01 20:28:03,970 - INFO - [SeleniumCrawler] Finding login input web element
2019-05-01 20:28:04,269 - INFO - [SeleniumCrawler] Send email to login input web element}
2019-05-01 20:28:04,416 - INFO - [SeleniumCrawler] Finding password input web element
2019-05-01 20:28:04,433 - INFO - [SeleniumCrawler] Send password to password input web element}
2019-05-01 20:28:04,568 - INFO - [SeleniumCrawler] Send Enter key pressing to password input web element}
2019-05-01 20:28:08,661 - INFO - [SeleniumCrawler] Finding account link
2019-05-01 20:28:08,730 - INFO - [SeleniumCrawler] Click on account link
2019-05-01 20:28:09,209 - INFO - [SeleniumCrawler] Extracting total friends amount value
2019-05-01 20:28:10,181 - INFO - [SeleniumCrawler] Finding friends page link
2019-05-01 20:28:10,204 - INFO - [SeleniumCrawler] Click on friends page link
2019-05-01 20:28:10,454 - INFO - [SeleniumCrawler] Extracting account name
2019-05-01 20:28:11,162 - INFO - [SeleniumCrawler] Load friends list web elements
2019-05-01 20:28:11,175 - INFO - [SeleniumCrawler] Friends list can be scroll
2019-05-01 20:28:11,175 - INFO - [SeleniumCrawler] Scroll to last friends list element
2019-05-01 20:28:12,220 - INFO - [SeleniumCrawler] Load friends list web elements
2019-05-01 20:28:12,261 - INFO - [SeleniumCrawler] Friends list can be scroll
2019-05-01 20:28:12,261 - INFO - [SeleniumCrawler] Scroll to last friends list element
2019-05-01 20:28:13,326 - INFO - [SeleniumCrawler] Load friends list web elements
2019-05-01 20:28:13,363 - INFO - [SeleniumCrawler] Friends list can be scroll
2019-05-01 20:28:13,363 - INFO - [SeleniumCrawler] Scroll to last friends list element
2019-05-01 20:28:14,393 - INFO - [SeleniumCrawler] Load friends list web elements
2019-05-01 20:28:14,440 - INFO - [SeleniumCrawler] Full friends list already loaded
2019-05-01 20:28:14,440 - INFO - [SeleniumCrawler] Extract data from friends web elements list
2019-05-01 20:28:15,721 - INFO - [SeleniumCrawler] Closing web driver
2019-05-01 20:28:15,721 - INFO - [SeleniumCrawler] Closing selenium web driver

2019-05-01 20:28:15,785 - INFO - [ConsoleReporter] Start reporting

========== REPORT ==========
Account name - Yana Sysa
https://www.facebook.com/natasha.ins - Nat Ins
https://www.facebook.com/anna.kolomiytseva - Anna Kolomiytseva
https://www.facebook.com/yuliyagulyayeva - Julia Gulyayeva
https://www.facebook.com/profile.php?id=100012284415084 - Tatiana Polyakova
https://www.facebook.com/yana.tkachenko.96 - Yana Tkachenko
https://www.facebook.com/ann.pavlenko.94 - Anuta Anuta
https://www.facebook.com/enviniel - Mia Marchenko
https://www.facebook.com/daniela.daas.1 - Daniela Daas
https://www.facebook.com/profile.php?id=100015744632195 - Екатерина Привала
https://www.facebook.com/abramyan.n - Anastasia Abramian
https://www.facebook.com/irynalakotkina - Iryna Lakotkina
https://www.facebook.com/profile.php?id=100013232589502 - Анастасия Сакунова
https://www.facebook.com/victoria.boiko.35 - Victoria Boiko
https://www.facebook.com/alexxander.bondarenko - Oleksandr Bondarenko
https://www.facebook.com/profile.php?id=100024762277034 - Ирина Губская
https://www.facebook.com/katy.ivanishchenko - Katy Ivanishchenko
https://www.facebook.com/sofiya.sevastyanova - Sofiya Sevastyanova
https://www.facebook.com/virakuryko - Vira Kuryko
https://www.facebook.com/daria.omelchenko.o - Дарья Омельченко
https://www.facebook.com/profile.php?id=100023765910119 - Елена Зима
https://www.facebook.com/profile.php?id=100001799139595 - Валерия Николаенко
https://www.facebook.com/andres.martinez.710 - Andres Martinez
https://www.facebook.com/victoria.samokhina.35 - Victoria Samokhina
https://www.facebook.com/profile.php?id=100015521199983 - Оксана Марченко
https://www.facebook.com/profile.php?id=100013087565675 - Алексей Зенякин
https://www.facebook.com/m.korolkow - Maxim Korolkov
https://www.facebook.com/profile.php?id=100017204015909 - Алёна Сокол
https://www.facebook.com/irina.tuzko - Irina Tuzko
https://www.facebook.com/catherine.matiyko - Catherine Matiyko
https://www.facebook.com/darija.grishanova - Dariia Hrishanova
https://www.facebook.com/sophia.zimnitskaya - Sophia Zimnitskaya
https://www.facebook.com/diana.savina.528 - Diana Savina
https://www.facebook.com/olga.petryk - Оля Петрик
https://www.facebook.com/profile.php?id=100006265891198 - Yulya Izvarina
https://www.facebook.com/profile.php?id=100001989543966 - Kseniia Shokalo
https://www.facebook.com/elinor.martiyan - Eleonora Martiian
https://www.facebook.com/varikvn - Вартан Назарьян
https://www.facebook.com/darya.rybalchenko.7 - Darya Rybalchenko
https://www.facebook.com/elina.matyash - Elina Matiash
https://www.facebook.com/Natalia.Igronova - Natalia Odessa Guide
https://www.facebook.com/darialtd - Дар'я Горбатовська
https://www.facebook.com/anya.pavlova.5 - Anna Greentree
https://www.facebook.com/bohdan.yeromenko.1 - Bohdan Yeromenko
https://www.facebook.com/leila.gurban - Leila Gurbanova
https://www.facebook.com/oles.petik - Oles Petik
https://www.facebook.com/profile.php?id=100013793352975 - Olena Dunaieva
https://www.facebook.com/andrey.shulika.1 - Andrey Shulika
https://www.facebook.com/alina.komisarova - Аліна Комісарова
https://www.facebook.com/anya.bulava - Anya Bulava
https://www.facebook.com/olga.buldina.1 - Olga Buldina
https://www.facebook.com/vera.shvayko.7 - Vera Shvayko
https://www.facebook.com/solomiia.english - Solomiia English
https://www.facebook.com/tatafomenkoo - Tatyana Fomenko
https://www.facebook.com/profile.php?id=100011484135034 - Игорь Жуков
https://www.facebook.com/ProfIT.kh - Ольга Пронина
https://www.facebook.com/profile.php?id=100009439515371 - Полина Белкина
https://www.facebook.com/gabriele.lagonigro - Gabriele Lagonigro
https://www.facebook.com/ilingua.school - ILingua LS
Total friends amount - 60
Scanned friends amount - 58
========== REPORT END ==========

2019-05-01 20:28:15,785 - INFO - [ConsoleReporter] Reporting finished

2019-05-01 20:28:15,785 - INFO - [Launcher] Program finished```