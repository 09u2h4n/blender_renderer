import os
import bpy
import json

def image_settings(blend_file_name="", output_path="default", resolution_x=1920, resolution_y=1080, output_extension="PNG", current_frame=None, engine='CYCLES', samples=100, cycles_device='GPU', use_file_setting=False):
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
    - cycles_device (str): Device for rendering ("CPU", "CUDA", "OPTIX", "HIP", "ONEAPI", "METAL").
    - current_frame (int or None): Current frame to render. If None, renders the current frame of the active scene.
    """
    # Activate all available devices
    for scene in bpy.data.scenes:
        scene.cycles.device = cycles_device

    prefs = bpy.context.preferences
    cprefs = prefs.addons['cycles'].preferences

    # Set the compute device type based on the cycles_device parameter
    if cycles_device == 'GPU':
        if 'CUDA' in cprefs.get_device_types():
            cprefs.compute_device_type = 'CUDA'
        elif 'OPTIX' in cprefs.get_device_types():
            cprefs.compute_device_type = 'OPTIX'
        elif 'HIP' in cprefs.get_device_types():
            cprefs.compute_device_type = 'HIP'
        elif 'ONEAPI' in cprefs.get_device_types():
            cprefs.compute_device_type = 'ONEAPI'
        elif 'METAL' in cprefs.get_device_types():
            cprefs.compute_device_type = 'METAL'
    else:
        cprefs.compute_device_type = 'NONE'  # Use CPU

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
    cycles_device = json_data["cycles_device"]

    image_settings(output_extension=output_extension, resolution_x=resolution_x, resolution_y=resolution_y, engine=engine, samples=samples, cycles_device=cycles_device, current_frame=current_frame, use_file_setting=use_file_setting)
