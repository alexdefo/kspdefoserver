# kspdefoserver


Настройка клиента и сервера для KSP
https://d-mp.org/

##Сервер KSP DMP Server.
(DMPServer.exe) exe — шник., socket сервер который по сети запоминает положение кораблей для всех.

DMPServer windows приложение, но работает на linux под mono. 
т.е. сервер можно держать на хостинге. 

для чистки серверной части полезно знать:
после запуска программа генерит папку Universe
там появляются папки

Players — там понятно что…
Kerbals — там конфиги персонажей
и самое главное Vessels — там файлики, с описанием текущих кораблей в вашей Universe…





##  Config/Settings.txt
Название сервера, порт, ограничения….
## DMPModControl.txt
!optional–files
все dll ки из GameData

!partslist
Название разрешенных деталек.

это все cfg файлы в подпапках parts., где само имя указано в самом файле в первой секции name
если там есть _ (нижн подчеркивание) его заменить на "."(точку).


