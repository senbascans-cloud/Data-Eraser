# 🔒 Secure Data Eraser – Community Edition

> **“Askeri sınıf veri imhanın açık kaynak önizlemesi”**  
> *Bu proje, gerçek askeri standartlara sahip ticari ürünümüzün demo sürümüdür. Kaynak kodu herkese açıktır, ancak en gelişmiş özellikler ve sertifikalar yalnızca kurumsal lisans ile sunulmaktadır.*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/License-GPLv3-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20WSL-lightgrey?style=for-the-badge" />
  <a href="https://www.virustotal.com/gui/file-analysis/ZWQyODkzZjliZjFjZmE3NTk3N2IwZGQ1OTAzYTEyYzY6MTc3NDU0OTM2MA==">
    <img src="https://img.shields.io/badge/VirusTotal-0%2F60%20(Build%20Temiz)-brightgreen?style=for-the-badge&logo=virustotal" />
  </a>
</p>

---

## 🎯 Proje Hakkında

**Secure Data Eraser – Community Edition**, dosyaları ve depolama aygıtlarını kurtarılamaz şekilde silmek için geliştirilmiş bir Python aracıdır.  
Bu sürüm, aşağıdaki temel silme algoritmalarını içerir:

- `zero` – sıfırlarla üzerine yazma  
- `random` – rastgele veri yazma  
- `dod3` – DoD 5220.22-M 3 geçiş (0x00, 0xFF, rastgele)  
- `dod7` – DoD 5220.22-M 7 geçiş (ECE standardı)

**Ancak bu, yalnızca bir “demo”dur.**  
Gerçek askeri standartlara (NIST SP 800-88, NATO sınıflandırması, donanım seviyesi doğrulama, ATA Secure Erase, uzaktan imha yönetimi) tam uyumlu **kurumsal sürüm**, henüz kamuya açıklanmamıştır. Bu projeyi yayınlamamızın amacı, yeteneklerimizi sergilemek ve ticari lisans için potansiyel müşterilere ulaşmaktır.

---

## 🖼️ Güvenlik & Şeffaflık

Kodumuz **VirusTotal** tarafından taranmış ve **tamamen temiz** raporlanmıştır.  
Aşağıdaki butondan detaylı analizi inceleyebilirsiniz:

<p align="center">
  <a href="https://www.virustotal.com/gui/file-analysis/ZWQyODkzZjliZjFjZmE3NTk3N2IwZGQ1OTAzYTEyYzY6MTc3NDU0OTM2MA==">
    <img src="https://img.shields.io/badge/🔍%20VirusTotal%20Analizini%20Görüntüle-00A98F?style=for-the-badge&logo=virustotal&logoColor=white" />
  </a>
</p>

> *Not: Yukarıdaki badge, yazılımın herhangi bir zararlı içermediğini kanıtlar. Bu açık kaynak demo, güvenlik konusunda en yüksek şeffaflıkla sunulmuştur.*

---

## 🧪 Neden Bu Proje Açık Kaynak?

- **Güven İnşa Etmek:** Müşterilerimiz, kodun içini görebilir, inceleyebilir ve kendi güvenlik testlerini yapabilir.
- **Topluluk Katkısı:** Hata bildirimleri ve algoritma geliştirmeleriyle ürünü birlikte büyütmek.
- **Ticari Ürünün Vitrini:** Gerçek askeri sınıf ürünümüzün yeteneklerini göstermek.

> **Önemli:** Bu community sürümü, aşağıdaki özellikleri **içermez**. Bunlar yalnızca kurumsal lisans ile sunulmaktadır.

| Özellik | Community Edition | Enterprise Edition |
|---------|-------------------|--------------------|
| DoD 5220.22-M (3/7 pass) | ✅ | ✅ |
| NIST SP 800-88 uyumluluk | ❌ | ✅ |
| NATO sınıflandırma entegrasyonu | ❌ | ✅ |
| ATA Secure Erase (SSD) | ❌ | ✅ |
| Donanım seviyesi doğrulama | ❌ | ✅ |
| Uzaktan yönetim konsolu | ❌ | ✅ |
| Kaynak kod erişimi (full) | ✅ (GPL) | ✅ (Özel) |
| 7/24 destek ve SLA | ❌ | ✅ |
| Sertifikasyon raporları | ❌ | ✅ |
| **Fiyat** | **Ücretsiz** | **Teklif bazlı** |

---

## 💼 Ticari Sürüm & Fiyatlandırma

Kurumsal lisans ile **Secure Data Eraser – Enterprise**’u satın alabilir, askeri standartlara tam uyumlu, donanım seviyesinde imha garantili çözümümüzü işletmenize entegre edebilirsiniz.

**Teklif almak ve detaylı bilgi için aşağıdaki butona tıklayın:**

<p align="center">
  <a href="https://caruppsecurity.com/fiyat.html">
    <img src="https://img.shields.io/badge/🎯%20Ticari%20Sürüm%20Teklifi%20Al-%20Hemen%20İncele-0a66c2?style=for-the-badge&logo=internetexplorer&logoColor=white" />
  </a>
</p>

*(Buton, sizi güncel fiyat listesi ve iletişim formuna yönlendirecektir.)*

---

## 📥 Kurulum & Kullanım

### 1. Depoyu klonlayın
```bash
git clone https://github.com/senbascans-cloud/Data-Eraser.git
cd Data-Eraser
