# Zadanie 1: konfiguracja oprogramowania
## Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?
Moją **główną** motywacją do wzięcia udziału w *DareIT Challenge* była pewna dziewczynka o imieniu Celina 

![Bez nazwy](https://user-images.githubusercontent.com/38132455/229228234-a3c481b8-aacd-4d13-8356-3f2449815c87.jpg)

Chciałabym pracować w domu 🏡 i samodzielnie ustalać najlepszą porę do pracy ⌚
Dodatkowym celem jest wyjazd do Szwecji i szybkie podjęcie tam pracy. Co mam nadzieję osiągnę dzięki DareIT ❤️

# "ZADANIE 2: selektory"
1. Login
* //*[@id="login"]
* //*[@name="login"]
* //input[@type="text"]

2. Password
* //input[@type="passwprd"]
* //*[@id="password"]
* //*[@name="password"]

3. Button "sign in"
* //*[@id="__next"]/form/div/div[2]/button
* //*[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss5 MuiButton-containedPrimary"]
* //*[contains(@class, "MuiButton-root")]

4. English
* //*[contains(@class, "MuiSelect-selectMenu")]
* //*[text()="English"]
* /html/body/div/form/div/div[2]/div/div
