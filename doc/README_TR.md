---
[Turkish](https://github.com/09u2h4n/blender_renderer/blob/main/doc/README_TR.md) | [English](https://github.com/09u2h4n/blender_renderer/blob/main/README.md)
---

# **Colab'ta Blender Renderer**
".blend" uzantılı dosyaları renderlar.

[![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/github/09u2h4n/blender_renderer/blob/main/blender_renderer_v01.ipynb)

## 🌀 **Blender Kullanımını Ayarla**

- `blender_ver` (Blender sürümü): Blender'ı indirecek ve yolunu ayarlayacak.

## 🖼️ **Tek Bir Görüntüyü Oluştur**

- `file_name` (Oluşturulacak dosya adı): "(file_name).blend" formatında olmalı, örneğin chess.blend.

- `thread_num` (Thread sayısı): İşlem ve render için kullanılacak thread sayısı [1-1024], sistem işlemci sayısı için 0.

- `render_engine` (Render motoru): Render motorunu belirtin.

- `frame_number` (Kare numarası): Belirli bir kareyi oluşturun. Örnek: `frame_number=10`, 10. kareyi oluşturur.

- `cycles_device` (Cycles cihazı): Kareleri oluşturmak için kullanılacak cihazı değiştirin.

- `hybrid_rendering` (Hybrid render): Bu seçili ise, CPU ve GPU kullanarak render denemesi yapacak. Ancak, eğer `cycles_device` olarak CPU seçilirse hybrid render yapılamaz.

## 📽️ **Animasyon Oluştur**

- `file_name` (Oluşturulacak dosya adı): "(file_name).blend" formatında olmalı, örneğin chess.blend.

- `thread_num` (Thread sayısı): İşlem ve render için kullanılacak thread sayısı [1-1024], sistem işlemci sayısı için 0.

- `render_engine` (Render motoru): Render motorunu belirtin.

- `use_file_s_frame_settings` (Dosyanın kare ayarlarını kullan): Dosyanın kare ayarlarını kullanır. Eğer bu seçili ise, kendi kare ayarlarını kullanamazsınız.

- `cycles_device` (Cycles cihazı): Kareleri oluşturmak için kullanılacak cihazı değiştirin.

- `hybrid_rendering` (Hybrid render): Bu seçili ise, CPU ve GPU kullanarak render denemesi yapacak. Ancak, eğer `cycles_device` olarak CPU seçilirse hybrid render yapılamaz.

### 📅 **Kare Ayarları**

- `start_frame` (Başlangıç karesi): Render edilecek karelerin başlangıcı.

- `end_frame` (Bitiş karesi): Render edilecek karelerin sonu.

- `jump_frame` (Atlama karesi): Atlama karesini ayarlar. Önceki ve sonraki karelerin çıkarılması.

- `fps` (Saniyedeki Kare Sayısı): Kare başına saniyedeki kare sayısını ayarlar.
