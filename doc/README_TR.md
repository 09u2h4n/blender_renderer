---
[Türkçe](https://github.com/09u2h4n/blender_renderer/blob/main/doc/README_TR.md) | [İngilizce](https://github.com/09u2h4n/blender_renderer/blob/main/README.md)
---

# **Colab'da Blender Renderlayıcı**

".blend" uzantılı blender dosyasını renderler.

[![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/github/09u2h4n/blender_renderer/blob/main/blender_renderer_v02.ipynb)

## 🌀 **Blender Kullanımı Ayarlama**

-   `blender_ver` (Blender sürümü): Blender'ı indirip yolunu ayarlayacak.

## 🖼️ **Tek Resim Renderlama Kullanımı**

-   `file_name` (Renderlanacak dosya adı): "(dosya_adı).blend" formatında olacak, örneğin chess.blend.
    
-   `thread_num` (İş parçacığı sayısı): Renderlama ve diğer işlemler için iş parçacığı sayısını kullanın [1-1024], sistem işlemci sayısı için 0.
    
-   `render_engine` (Render motoru): Render motorunu belirtin.
    
-   `frame_number` (Kare numarası): Belirli bir kareyi renderlayın. Örneğin, `frame_number=10` 10. kareyi renderlar.
    
-   `cycles_device` (Cycles cihazı): Render karelerini renderlemek için kullanılan cihazı geçersiz kılar.
    

## 📽️ **Animasyon Renderlama Kullanımı**

-   `file_name` (Renderlanacak dosya adı): "(dosya_adı).blend" formatında olacak, örneğin chess.blend.
    
-   `thread_num` (İş parçacığı sayısı): Renderlama ve diğer işlemler için iş parçacığı sayısını kullanın [1-1024], sistem işlemci sayısı için 0.
    
-   `render_engine` (Render motoru): Render motorunu belirtin.
    
-   `cycles_device` (Cycles cihazı): Render karelerini renderlemek için kullanılan cihazı geçersiz kılar.
    

### 📅 **Kare Ayarları**

-   `use_file_s_frame_settings` (Dosyanın kare ayarlarını kullan): Dosyanın kare ayarlarını kullanır. İşaretlendiğinde, karelerin kendi ayarlarını kullanamazsınız.
    
-   `start_frame` (Başlangıç karesi): Renderlanacak kare aralığının başlangıcı.
    
-   `end_frame` (Bitiş karesi): Renderlanacak kare aralığının sonu.
    
-   `jump_frame` (Atlama karesi): Bir sonraki ve bir önceki kareleri çıkarmak için kare aralığını ayarlar.
    
-   `fps` (Saniyedeki kare sayısı): Saniyedeki kare sayısını ayarlar.
