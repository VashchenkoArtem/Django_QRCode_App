# Генератор QR-кодів/QR-Code generator
---
## Генератор QR-кодів - проєкт, який був створений для створювання кастомізованих QR-кодів, які користувач зберігає на сайті
QR Code Generator is a project that was created to create customized QR codes that the user saves on the site.
---
## Знаходячись на сайті ви можете: 
- **Створити акаунт**
- **Увійти в акаунт**
- **Створити** QR-код
- **Кастомізувати** та **видаляти** QR-код
- **Зв'язатися** з розробниками
- **Задати** та **змінити** підписку

## While on the site you can: 
- **Create an account**
- **Log in to your account**
- **Create** a QR code
- **Customize** and **delete** a QR code
- **Contact** the developers
- **Set** and **change** a subscription

## Ціль проєкта
Нашою **ціллю** було **створення зручного генераторат QR-кодів**, де людина може **обрати** будь-яку **кастомізацію**

## Над цим проєктом працювали/They worked on the project:
**Ващенко Артем(TeamLead)**: https://github.com/VashchenkoArtem
**Кирило Харлан**: https://github.com/KirillKharlan
**Марков Дмитро**: https://github.com/DmitriyM08
**Архіп Гончар**: https://github.com/Arhip-ops

## Посилання на figma дизайн/ Link on figma design file: 
https://www.figma.com/design/09TXxVuloOwYY96sCny7ie/Design-For-QR-Code-Practice?node-id=0-1&p=f&t=3qrRc0rj35zyk61W-0

Цей проєкт **корисний** для **початківців** тим, що під час **праці** над ним **задіюється робота** з **базами даних**, **CSS** та **HTML**.

This project is **useful** for **beginners** because **working** on it **involves** working with **databases**, **CSS**, and **HTML**.

## В проєкті **використовувались** такі **бібліотеки**:
- **Django** (**Створення** сайту)
- **Qrcode** (**Робота** з **qr-кодами**)
- **Pillow** (**Робота** з **зображеннями**)

## The following **libraries** were **used** in the project:
- **Django** (**Creating** a website)
- **Qrcode** (**Working** with **qr-codes**)
- **Pillow** (**Working** with **images**)

## Як запустити проєкт локально?/How to run a project locally?

1. **Встановіть Git** та **VisualStudioCode**, якщо ще **не встановлено** \ **Install Git** and **VisualStudioCode** if **not already installed**
2. **Відкрийтe VisualStudioCode** \  **Open VisualStudioCode**
3. **Створіть** або **відкрийте** необхідну **папку**, в якій буде знаходитися **проєкт** \ **Create** or **open** the necessary **folder** where the **project** will be located.
4.**Відкрийте термінал** і **пропишіть** \ **Open a terminal** and **type**:
```python
git clone https://github.com/VashchenkoArtem/Django_QRCode_App
```
5. **Створіть** **віртуальне оточення** \ **Create a virtual env**:
```python
python -m venv <namevenv>
```
6. **Активуйте** його \ **Activate** it:
###  MacOS та Linux
```python
source <namevenv>/bin/activate
```
### Windows 
```python
.\<namevenv>\Scripts\activate.bat
```
7. **Встановіть** необхідні **бібліотеки** в **віртуальне оточення** з файлу **requirements.txt** 
**Install** the required **libraries** into the **virtual environment** from the **requirements.txt** file
```python
pip install -r requirements.txt
```
8. **Перейдіть** в папку **Django_QRCode_App**, якщо ви **не там** \ **Go** to the **Django_QRCode_App** folder if you are **not there**
```python
cd Django_QRCode_App
```
9. **Запустіть** сервер \ **Run** the server
```python
python manage.py runserver
```
10.  **Натисніть** на **посилання** \ **Click** on **link**:
![](images_readme/run_server.png)

11.  Вітаємо! Ви **локально** **запустили** проєкт! \\ Congratulations! You have **locally** **launched** the project!

## Структура проєкта \ Structure of project
![](images_readme/structure.png)

## За що відповідає кожен з додатків? \ What is each application responsible for?

- ### **Додаток home_app** \ **Application home_app**
![](images_readme/main_page.png)
Додаток **home_app** відповідає за **головну** сторінку. Тобто **відображення** усього **функціоналу** сайту. Наприклад: Виду **підписок** або **генерування** QR-коду \ The **home_app** application is responsible for the **main** page. That is, **displaying** all **functionality** of the site. For example: Viewing **subscriptions** or **generating** a QR code

- ### Додаток registration1 \ Registration1 application
![](images_readme/registration1_page.png)
Додаток **registration1** відповідає за **заповнення форми**, яка потім **відправляється на обробку на сервер**. Якщо **форма** заповнена **правильно** - **користувача реєструє** в **базу** **даних** та **перекидує** на іншу **сторінку** \ The **registration1** application is responsible for **filling out the form**, which is then **sent to the server for processing**. If the **form** is filled in **correctly** - it **registers** the user** into the **database** and **redirects** him/her** to another **page**

### Додаток registration3 \ Registration3 application
![](images_readme/registration_3.png)
Додаток **registration3** відповідає за **успішну реєстрацію**. Після **натискання** на кнопку **"Авторизація"** - користувача **перекидує** на **авторизацію** \ The **registration3** application is responsible for **successful registration**. After **clicking** on the **"Authorization"** button - the user **is redirected** to **authorization**

### Додаток authorithation1 \ Authorithation1 application
![](images_readme/authorithation1.png)
Додаток **authorithation1** відповідає за **авторизацію** користувача. Користувач **заповнює** форму та якщо вона **правильно заповнена** - користувач **переходе** на **2 етап перевірки** \ The **authorithation1** application is responsible for **authorization** of the user. The user **fills** in the form and if it is **correctly filled** in - the user **proceeds** to **stage 2 of verification**

### Додаток authorithation2 \ Authorithation2 application
![](images_readme/authorithation2.png)
Додаток **authorithation2** відповідає за **відправку повідомлення на пошту**, яку **вказав** користувач. Ця сторінка **служить** **другим етапом перевірки** \ The **authorithation2** application is responsible for **sending a message to the email address** that the user **specified**. This page **serves** as the **second stage of verification**

### Додаток authorithation3 \ Authorithation3 application
![](images_readme/authorithation3.png)
Додаток **authorithation3** відповідає за **успішну авторизацію**. Якщо все пройшло **успішно** - людину **авторизує** та **перекидає** на **головну** / The **authorithation3** application is responsible for **successful authorization**. If everything went **successfully**, it **authorizes** the person and **transfers** them to the **main** page.

### Додаток subscribe \ Subscribe application
![](images_readme/subscribe.png)
Додаток **subscribe** відповідає за **задання підписки** користувачу, в залежності від того, на яке **посилання** він **натисне** на **головній сторінці**. \ The **subscribe** application is responsible for **assigning** a subscription to a user, depending on which **link** they **click** on the **homepage**.
#### Види підписок: \ Types of subscriptions:

-  **Free** (**1 безкоштовний** qr-код на **6 місяців**) \ **Free** (**1 free** QR code for **6 months**)
  
- **Standart** (**10 qr-кодів** на **6 місяців** за **2\$** за місяць) \ **Standart** (**10 QR codes** for **6 months** for **$2** per month)

- **Pro** (**100 qr-кодів** на **6 місяців** за **10\$** за місяць) \ **Pro** (**100 QR codes** for **6 months** for **$10** per month)

- **Desktop** (**5**, **10** або **20 qr-кодів** з **посиланням** на **desktop** додатки на **6 місяців** за **50 центів**, **1\$** або **2\$**)  **Desktop** (**5**, **10** or **20 QR codes** with a **link** to the **desktop** application for **6 months** for **50 cents**, **1\$** or **2\$**)

### Додаток qrgenerate_app \ Qrgenerate_app application
![](images_readme/generate_qr.png)
Додаток **qrgenerate_app** відповідає за **генерацію будь-якого qr-кода**, якщо **користувач** ще **може** робити **qr-коди**. Якщо у **користувача** вже є **максимальна кількість qr-кодів**, яка **вказана** в **підписці** - йому **виведе попередження** та **qr-код не створиться**. \ The **qrgenerate_app** application is responsible for **generating any qr code** if the **user** can still **make **qr codes**. If the **user** already has the **maximum number of qr codes**, which is **specified** in the **subscription** - he will **get a warning** and **the qr code will not be created**.

### Додаток my_codes \ My_codes application
![](images_readme/my_codes.png)
Додаток **my_codes** відповідає за **збереження усіх qr-кодів**, які **створив** користувач. Користувач може **переглянути** **більшe** даних про **qr-код**, **натиснувши** на **назву qr-кода**. Якщо у користувача **завершилася підписка** - у нього буде працювати лише **1**, **останньо створенний qr-код**, а **всі інші** **заблокуються**. \ The **my_codes** application is responsible for **saving all qr-codes** that **the user has created**. The user can **view** **more** data about the **qr-code** by **clicking** on the **qr-code name**. If the user has **expired their subscription** - only **1**, **the last created qr-code** will work, and **all others** will **be blocked**.

### Додаток contacts \ Contacts application

![](images_readme/contacts.png)
Додаток **contacts** відповідає за **зворотній зв'язок до розробників**. \ The **contacts** application is responsible for **feedback to developers**.

### Папка media \ Media folder

В **проєкті** ми **використали** папку "**media**", як папку, в якій **зберігаються** всі **медійні файли**(**в нашому випадку qr-коди**). \ In the **project** we **used** the "**media**" folder as the folder in which **all** media files** (**in our case, QR codes**) are **stored**.

### Додаток images_readme \ Images_readme folder

Цю **папку** було **створено** для **збереження** в ній **зображень**, які ми **відобразили** в файлі **readme.md**. \ This **folder** was **created** to **store** the **images** that we **displayed** in the **readme.md** file.

### Папка templates \ Templates folder

В цій **папці** ми **створили базовий html шаблон**, який ми **використовували** для **інших додатків**. \ In this **folder** we **created a basic html template** that we **used** for **other applications**.

### Файл .gitignore \ .gitignore file 

В цьому **файлі** ми **задаємо папки** або **файли**, які ми **не включаємо** в **commit**. \ In this **file** we **specify folders** or **files** that we **do not** include in the **commit**.

### Файл db.sqlite3 \ Db.sqlite3 file

Це наша **база даних**, в якіх **зберігаються** **таблиці** по типу: **django_session**, **auth_user**... \ This is our **database**, which **stores** **tables** of the following types: **django_session**, **auth_user**...

### Файл manage.py \ Manage.py file

Цей **файл** ми **використовуємо** для **запуску проєкта**. \ We **use** this **file** to **launch the project**.

### Файл readme.md \ Readme.md file

Цей **файл** ми **використовуємо** для **опису** всього **проєкта** в ньому. \ We **use** this **file** to **describe** the entire **project** in it.

### Файл requirements.txt \ Requirements.txt file

В цьому **файлі** ми **створили** всі **необхідні** **бібліотеки** та їх **версії** для **запуску проєкта**. \ In this **file** we **created** all the **necessary** **libraries** and their **versions** to **launch the project**.

## Приклад створення django-проєкта \ Example of creating a django-project
1. **Встановіть віртуальне оточення** \ **Set venv**
2. **Активуйте** його \ **Activate** it
3. **Встановіть** в нього **бібліотеку django**: \ **Install** the **django library** into it:
```python
pip install django
```
4. **Створіть проєкт**: \ **Create project**
```python
python django-admin startproject <project_name>
```
5. Це **все**, що **потребується** для **створення** звичайного **проєкта**. Але, якщо ви будете **працювати** з **media-файлами** - вам **необхідно створити** нові **константи** для **налаштування** у файлі **settings.py** \ This is **all** that is **needed** to **create** a regular **project**. But, if you **will** be **working** with **media files** - you **need** to create** new **constants** for **settings** in the **settings.py** file
```python
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
6. Вітаємо! Ви **створили** проєкт! Тепер, давайте **перейдемо** до **створення додатків**. \ Congratulations! You **created** a project! Now, let's **move** to **building apps**.

## Приклад створення додатку \ Example of creating application

1. У вас **повинен** бути **django-проєкт**. Якщо **нема** - **створіть** його. \ You **must** have a **django project**. If you **don't** have one, **create** one.
2. **Пропишіть** в **терміналі**: \ **Write** in **terminal**:
```python
python manage.py startapp <application_name>
```
Ви **обов'язково** повинні **находитись** в **дерикторії проєкта**. \ You **must** be **located** in the **project directory**.
3. У вас **створився** **додаток**. Давайте **налаштуємо** його: \ You have **created** an **application**. Let's **configure** it:
- **Перейдіть** в **settings.py** та **знайдіть** там **константу INSTALLED_APPS**. **В кінці додайте назву** свого **додатку**: \ **Go** to **settings.py** and **find** the **INSTALLED_APPS** constant there. **At the end, add the name** of your **application**:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'your_application_name'
]
```
- У **додатку**, **створіть** папку **templates** та в ній ще одну **папку**** з назвою додатку**, а в ній вже **html-шаблон**. Тобто, ваша **дерикторія**, **починаючи** з **templates** повинна **виглядати** так: \ In the **application**, **create** a **templates** folder and in it another **folder**** with the name of the application**, and in it an **html template**. That is, your **directory**, **starting** with **templates** should **look** like this:
```html
templates/<your_application_name>/index.html
```
- **Створіть** необхідну **структуру** в **html-документі** \ **Create** the required **structure** in the **html document**
- У файлі **views.py створіть функцію відображення** сторінки з **назвою**, наприклад: **render_home_page**. Вона **приймає необхідний параметр request**. Якщо хочете, щоб у вас **відображалися** **підказки** у цій функції - вам необхідно **уточнити параметр request**. Для цього вам необхідно **імпортувати** з **django.http HttpRequest**: \ In the **views.py file, create a function to render** the page with a **name**, for example: **render_home_page**. It **accepts the required request** parameter. If you want to **display** **tooltips** in this function - you need to **specify the request** parameter. To do this, you need to **import** from **django.http HttpRequest**:
```python
from django.http import HttpRequest


def render_home_page(request: HttpRequest):
```
- Після цього, **повертаємо** в функції **відображену сторінку**, завдяки методу **render**. У нього є **2 необхідних параметра**. **Перший** параметр - **request**, а **другий** параметр - **шлях до html-шаблона**, починаючи від папки **templates**: \ After that, we **return** the **rendered page** to the function, thanks to the **render** method. It has **2 required parameters**. The **first** parameter is **request**, and the **second** parameter is **the path to the html template**, starting from the **templates** folder:
```python
    return render(request, template_name = "<name_folder_in_templates>/index.html")
```
- Тепер, нам необхідно **додати** цій функції відображення **url**. Але тут є **2** способи: \ Now, we need to **add** this **url** mapping function. But there are **2** ways:
### I Спосіб (створення посилання у головному url) \ Method I (creating a link in the main url)
1. **Заходимо** в urls.py проєкта \ **Go** to the project's urls.py
2. **Імпортуємо** сюди нашу **функцію відображення**: \ **Import** our **map function** here:
```python
from <name_application>.views import <name_render>
```
3. **Додаємо** нове **посилання** в **urlpatterns**, завдяки методу **path** \ **We** add a new **link** to **urlpatterns**, thanks to the **path** method
```python
    path("/Adress/", <name_render>)
```
В цьому випадку, **перший** параметр - **адреса посилання**, а **другий** параметр - **функція відображення** \ In this case, the **first** parameter is the **link address**, and the **second** parameter is the **display function**
### II Спосіб (створення посилання у власному urls.py) \ Method II (creating a link in your own urls.py)
Якщо ви в майбутньому **збираєтесь** робити ще **посилання**, які **однакові** з цим - вам краще **зробити** **ще один urls.py**, щоб **не повторювати адреси** \ If you **are** going to make more **links** that are **the same** as this one in the future - you'd better **make** **another urls.py** to **not repeat addresses**.
1. **Створіть** у **додатку** **власний urls.py** \ **Створіть** у **додатку** **власний urls.py**
2. В ньому **імпортуйте** ті ж методи **django**, які **імпортовані** в **головному** urls.py \ In it, **import** the same **django** methods that are **imported** in **main** urls.py.
3. **Створіть** такий ж об'єкт **urlpatterns** та **створіть** в ньому **посилання**: \ **Create** the same **urlpatterns** object and **create** a **link** in it:
```python
urlpatterns = [
    path("/Adress/", <name_render>)
]
```
4. **Переходимо** в **головний** urls.py та разом з **функцією path імпортуємо include** \ **Go** to **main** urls.py and import include** along with **path function**
5. **Робимо посилання**, яке при **наявності** в **адресі** вказаного **url** буде **включати** в себе **інші посилання** за цією **адресою** \ **We create a link** that, if the specified **url** is present in the **address**, will **include** other links** at this **address**
```python
path("Adress1/", include("<path_to_urls.py>"))
```
В цьому випадку, якщо користувач **перейде** за **адресою** Adress1, то у нього **буде** **вибір** **перейти** на ішні **адреси**, які ми **вказали** **в власному urls.py** \ In this case, if the user **goes** to **address** Adress1, then he **will** have the **choice** to **go** to other **addresses** that we **specified** **in our own urls.py**
- Вітаємо! Ви **створили** особистий **додаток**! \ Congratulations! You **created** your personal **app**!

## Views.py, index.html та models.py, які були створенні у нашому проєкті
Всі наші views.py з точним описом ви можете знайти, перейшовши за посиланням: <a href = "readme_files/all_views.md">asdas</a>