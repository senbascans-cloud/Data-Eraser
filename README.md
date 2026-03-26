# Secure Data Eraser – Community Edition

**Güvenli veri imha aracı** – Dosyaları veya depolama aygıtlarını (USB, HDD, SSD) kurtarılamaz şekilde siler.  
DoD 5220.22-M (3 ve 7 geçiş), sıfırlama ve rastgele veri yazma yöntemlerini destekler.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

---

## 📌 Özellikler

- **Dosya silme** (`--file`) veya **blok aygıt silme** (`--device`) desteği  
- **Silme yöntemleri**:
  - `zero` – sadece sıfır yazma  
  - `random` – rastgele veri yazma  
  - `dod3` – DoD 5220.22-M 3 geçiş (0x00, 0xFF, rastgele)  
  - `dod7` – DoD 5220.22-M 7 geçiş (ECE standardı)  
- **Doğrulama** seçeneği (`--verify`) – yazılan her bayt okunup kontrol edilir  
- İlerleme göstergesi ve geçiş süresi raporu  
- Root yetkisi gerektiğinde uyarı (aygıt silme)  
- Açık kaynak (GPLv3)

---

## 🚀 Gereksinimler

- Python 3.6 veya üzeri  
- Linux / macOS / WSL (Windows için WSL önerilir)  
- Aygıt silme işlemleri için **root** yetkisi (`sudo`)

---

## 📥 Kurulum

### 1. Depoyu klonlayın

python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# veya
venv\Scripts\activate      # Windows (WSL)

Çalıştırın
Herhangi bir ek paket kurulumu gerekmez – sadece standart Python kütüphaneleri kullanılır.

Dosya Silme
python secure_eraser.py --file gizli_belge.pdf --method dod3
Blok aygıt silme (örn. USB bellek – dikkat!)

Komut Satırı Seçenekleri
usage: secure_eraser.py [-h] (--file FILE | --device DEVICE)
                        [--method {zero,random,dod3,dod7}] [--verify] [--version]

Secure Data Eraser - Güvenli veri imha aracı (Community Edition)

options:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  Silinecek dosya yolu
  --device DEVICE, -d DEVICE
                        Silinecek blok aygıt yolu (örn. /dev/sdb)
  --method {zero,random,dod3,dod7}, -m {zero,random,dod3,dod7}
                        Silme yöntemi (varsayılan: dod3)
  --verify, -v          Her geçişten sonra yazılan veriyi doğrula (daha yavaş)
  --version             show program's version number and exit
sudo python secure_eraser.py --device /dev/sdc --method zero

git clone https://github.com/senbascans-cloud/Data-Eraser.git
cd Data-eraser

  SSD'lerde güvenilirlik
Flash tabanlı aygıtlar (SSD, USB bellek) üzerine yazma yöntemleri, denetleyicinin aşınma dengelemesi (wear leveling) nedeniyle her zaman başarılı olmayabilir. SSD'ler için ATA Secure Erase veya üretici araçları kullanılması önerilir.

Root yetkisi
Blok aygıt (/dev/sdX) silmek için sudo gereklidir. Program sizi uyaracaktır.

Geri dönüş yok
Silinen veriler kesinlikle kurtarılamaz. İşlemden önce mutlaka yedek alın.

Lisans
Bu yazılım GPL v3 ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

Copyright (C) 2026 Carupp Security

Bu program özgür yazılımdır: GNU Genel Kamu Lisansı sürüm 3 koşulları altında
dağıtabilir ve/veya değiştirebilirsiniz.
