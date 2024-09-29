# Bakapi Bag Script
Tento jednoduchý python script za pomocí knihovny [bakapi-v2](https://github.com/MortikCZ/bakapi-v2) dokáže zjistit rozvrh pro dnešní a zítřejší den a vypsat co si na zítra vyndat a naopak dát do tašky.

## Instalace
1. Stáhněte si tento repozitář
2. Nainstalujte si potřebné knihovny pomocí `pip install -r requirements.txt`
3. V souboru `app.py` vyplňte své údaje pro přihlášení do bakalářů.
```python
BAKALARI_URL = 'login-page-url'
BAKALARI_USERNAME = 'username' 
BAKALARI_PASSWORD = 'password'
```
- `BAKALARI_URL` je URL adresa stránky, kde se přihlašujete do bakalářů.
- `BAKALARI_USERNAME` je vaše uživatelské jméno.
- `BAKALARI_PASSWORD` je vaše heslo.
4. Spusťte script pomocí `python app.py`, takhle by měl vypadat výstup:
```python
Dnešní datum: 24.09.

Z tašky si vyndej:
Počítačové sítě
Základy přírodních věd

A do tašky si naopak dej:
Aplikační software

Přeji krásný den :)
```
## Changelog
- [**1.1**](https://github.com/MortikCZ/bakapi-bag-script/releases/tag/v1.1)
    - V případě že je dnešní den pátek, sobota či neděle script vypíše co si vyndat na pondělí.
- [**1.0**](https://github.com/MortikCZ/bakapi-bag-script/releases/tag/v1.0)
    - První verze scriptu.
    
