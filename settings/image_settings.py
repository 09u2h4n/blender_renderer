import os
import bpy
import sys
import subprocess
import json

def install_tqdm():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])

try:
    from tqdm import tqdm
except ImportError:
    install_tqdm()
    from tqdm import tqdm

def image_settings(blend_file_name="", output_path="default", resolution_x=1920, resolution_y=1080, output_extension="PNG", current_frame=None, engine='CYCLES', samples=100, device='GPU', use_file_setting=False):
    """
    Renders a Blender file and prints a progress bar to the terminal.

    Parameters:
    - blend_file_name (str): Name of the .blend file to render.
    - output_path (str): Path to save the rendered image. If "default", it will use the default output path.
    - output_extension (str): Extension of the output image (e.g., 'png', 'jpg', etc.).
    - resolution_x (int): Horizontal resolution of the output image.
    - resolution_y (int): Vertical resolution of the output image.
    - engine (str): Rendering engine to use (e.g., 'CYCLES', 'BLENDER_EEVEE', etc.).
    - samples (int): Number of render samples.
    - device (str): Device for rendering ("CPU", "CUDA", "OPTIX", "HIP", "ONEAPI", "METAL").
    - current_frame (int or None): Current frame to render. If None, renders the current frame of the active scene.
    """
    # Activate all available devices
    for scene in bpy.data.scenes:
        scene.cycles.device = device

    prefs = bpy.context.preferences
    cprefs = prefs.addons['cycles'].preferences

    # Calling this purges the device list so we need it
    cprefs.get_devices()

    # Attempt to set GPU device types if available
    for compute_device_type in ('CUDA', 'OPENCL'):
        try:
            cprefs.compute_device_type = compute_device_type
            break
        except TypeError:
            pass

    # Enable all CPU and GPU devices
    for device in cprefs.devices:
        device.use = True

    if not use_file_setting:
        # Set render resolution
        bpy.context.scene.render.resolution_x = resolution_x
        bpy.context.scene.render.resolution_y = resolution_y

        # Set render engine
        bpy.context.scene.render.engine = engine

        # Set current frame
        if current_frame is not None:
            bpy.context.scene.frame_set(current_frame)

        # Set render samples
        if engine == 'CYCLES':
            bpy.context.scene.cycles.samples = samples
        elif engine == 'BLENDER_EEVEE':
            bpy.context.scene.eevee.taa_render_samples = samples

        # Set output_extension
        bpy.context.scene.render.image_settings.file_format = output_extension.upper()

    bpy.ops.render.render(write_still=True)

if __name__ == "__main__":
    # Example usage
    settings_json_file_path = os.path.join(os.getcwd(), "settings", "settings.json")
    with open(settings_json_file_path) as file:
        json_data = json.load(file)

    use_file_setting = json_data["use_file_setting"]
    resolution_x = json_data["resolution_x"]
    resolution_y = json_data["resolution_y"]
    output_extension = json_data["output_extension"]
    current_frame = json_data["current_frame"]
    engine = json_data["engine"]
    samples = json_data["samples"]
    device = json_data["device"]

    image_settings(output_extension=output_extension, resolution_x=resolution_x, resolution_y=resolution_y, engine=engine, samples=samples, device=device, current_frame=current_frame, use_file_setting=use_file_setting)
