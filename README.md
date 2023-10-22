# **Blender Renderer on colab**
It renders blender file with ".blend" extensions.

[![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/github/09u2h4n/blender_renderer/blob/main/blender_renderer_v01.ipynb)

## 🌀 **Set Blender Usage**

- `blender_ver` (Blender version): It will download blender and set the path.

## 🖼️ **Render Single Image Usage**

- `file_name` (File name to render): It will be in "(file_name).blend" format, like chess.blend.

- `thread_num` (Thread number): Use the number of threads for rendering and other operations [1-1024], 0 for system's processor count.

- `render_engine` (Render engine): Specify the render engine.

- `frame_number` (Frame number): Render a specific frame. For example, `frame_number=10` will render the 10th frame.

- `cycles_device` (Cycles device): Override the device that is used to render frames.

- `hybrid_rendering` (Hybrid rendering): If checked, it will attempt to render using both CPU and GPU. However, if CPU is selected as the `cycles_device`, hybrid rendering is not possible.

## 📽️ **Render Animation Usage**

- `file_name` (File name to render): It will be in "(file_name).blend" format, like chess.blend.

- `thread_num` (Thread number): Use the number of threads for rendering and other operations [1-1024], 0 for system's processor count.

- `render_engine` (Render engine): Specify the render engine.

- `use_file_s_frame_settings` (Use file's frame settings): It uses the file's frame settings. If checked, you cannot use the frame's own settings.

- `cycles_device` (Cycles device): Override the device that is used to render frames.

- `hybrid_rendering` (Hybrid rendering): If checked, it will attempt to render using both CPU and GPU. However, if CPU is selected as the `cycles_device`, hybrid rendering is not possible.

### 📅 **Frame's Setting**

- `start_frame` (Start frame): Beginning of the frame range to render.

- `end_frame` (End frame): End of the frame range to render.

- `jump_frame` (Jump frame): It sets the frame interval for extracting next and previous frames.

- `fps` (Frames per second): It sets the frames per second.
