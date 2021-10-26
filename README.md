# defaut config içeriği:
```
top: 0.0378
```
İmajın tepesinden % 3.78'i kesilecek demektir.


Diğer eksenlerden kesmek istersek şu şekilde kullanılabilir:

```
top: 0.123
left: 0.123
right: 0.123
bottom: 0.123
```


# create executable

pip install .
pip install pyinstaller
pyinstaller labelme.spec
dist/orientis-labelme --version


