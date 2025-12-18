# Projelerle Yapay Zeka ve Bilgisayarlı Görü - Pratik Uygulamalar

![Durum](https://img.shields.io/badge/durum-devam%20ediyor-yellowgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-gray?logo=opencv)
![TensorFlow](https://img.shields.io/badge/TensorFlow-orange?logo=tensorflow)

Bu depo, **M. Ümit Aksoylu** tarafından yazılan **"Projelerle Yapay Zeka ve Bilgisayarlı Görü"** (Kodlab Yayınları) adlı kitaptaki projelerin ve alıştırmaların kişisel çözümlerimi içermektedir.

Kitabı bölüm bölüm çalışırken tamamladığım projeleri buraya ekliyorum. Amacım, kitaptaki teorik bilgileri pratiğe dökerek öğrenme sürecimi belgelemek ve pekiştirmektir.

## Kitap Hakkında

> **Kitap Adı:** Projelerle Yapay Zeka ve Bilgisayarlı Görü
> **Yazar:** M. Ümit Aksoylu
> **Yayınevi:** Kodlab
>
> Bu kitap, yapay zeka ve bilgisayarlı görü konularına giriş yapmak, temel teoriyi öğrenmek ve bu bilgileri Python, OpenCV, TensorFlow/Keras gibi popüler kütüphanelerle gerçek dünya projelerine uygulamak için kapsamlı bir kaynaktır.

## Kullanılan Teknolojiler

Bu depodaki projelerde ağırlıklı olarak aşağıdaki teknolojiler ve kütüphaneler kullanılmıştır:

* **Programlama Dili:** Python 3.x
* **Bilgisayarlı Görü:** OpenCV
* **Makine Öğrenmesi / Derin Öğrenme:** TensorFlow, Keras, Scikit-learn
* **Veri İşleme:** NumPy, Pandas
* **Görselleştirme:** Matplotlib

## Depo Yapısı

Projeler, kitaptaki ilerlemeye paralel olarak projeler adlı klasörde bulunmaktadır. Her biri ilgili proje veya bölümün adını taşır ve içerisinde gerekli kod dosyalarını (`.py` veya `.ipynb`), kullanılan veri setlerini (veya veri setlerine bağlantıları) ve projeye özel notları barındırır.

## Kurulum (Getting Started)

Projeleri yerel makinenizde çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Depoyu klonlayın:**
    ```bash
    git clone [https://github.com/](https://github.com/)[KULLANICI_ADINIZ]/[REPO_ADINIZ].git
    cd [REPO_ADINIZ]
    ```

2.  **Sanal Ortam Oluşturun (Önerilir):**
    Projelerin bağımlılıklarını sisteminizdeki diğer Python paketlerinden izole etmek için bir sanal ortam (virtual environment) oluşturmanız şiddetle tavsiye edilir.
    ```bash
    python -m venv venv
    ```
    Aktifleştirme:
    * Windows: `.\venv\Scripts\activate`
    * macOS/Linux: `source venv/bin/activate`

3.  **Bağımlılıkları Yükleyin:**
    Gerekli tüm kütüphaneler `requirements.txt` dosyasında listelenmiştir.
    ```bash
    pip install -r requirements.txt
    ```

## Projeleri Çalıştırma

Her proje klasörünün içine girerek ilgili Python betiğini çalıştırabilirsiniz.

Örnek olarak:

```bash
# Plaka Okuma Sistemi projesinin klasörüne gidin
cd Proje-03-Plaka-Okuma-Sistemi/

# Projeyi çalıştırın
python ocr.py --image test_images/plaka1.jpg
```

## Lisans

Bu depodaki kodlar, aksi belirtilmediği sürece MIT Lisansı altında lisanslanmıştır. Kitabın orijinal içeriği ve konseptleri yazarı M. Ümit Aksoylu'ya aittir.

# Teşekkür

Bu değerli kaynağı hazırladığı ve karmaşık konuları projelerle somutlaştırdığı için M. Ümit Aksoylu'ya teşekkürler.
