# Kullanım
* img_crop exe çalıştırıldığı zaman dizin seçme diyaloğu açılır.
* Seçilen dizindeki (sadece o klasörde bulunan) görüntü dosyalarının tümü taranır. Orjinal dosyalarda değişiklik yapılmaz.
* Seçilen dizin altına `_cropped_<crop edilme bilgisi>` isimli bir klasör yaratılır ve içerisine crop edilmiş görüntü dosyaları oluşturulur.

### Varsayılandan farklı bir crop işlemi yapılmak istenirse:
* img_crop exe'sinin bulunduğu yere bir config.yml dosyası oluşturulur. 
* Örmek:
```
top: 0.123
left: 0.123
right: 0.123
bottom: 0.123
```
* Her eksen verilmek zorunda değildir. Sadece belirtilen eksenler kesilir. (Top kesilmek istenmezse 0 verilmeli.)

# defaut crop:
```
top: 0.0378
```
İmajın tepesinden % 3.78'i kesilecek demektir.


# create executable

```
pip install .
pip install pyinstaller
pyinstaller --onefile img_crop.py
dist/img_crop
```

