from utils.utils import run_command
import os
import json

def run_blender_with_subprocess(render_animation = False):

    blender_path = os.getenv("BLENDER_PATH")

    settings_json_file_path = os.path.join(os.getcwd(), "settings", "settings.json")
    with open(settings_json_file_path) as file:
        json_data = json.load(file)

    blend_file_name = json_data["blend_file_name"]

    if os.sep not in blend_file_name:
        blend_file_path = os.path.join(os.getcwd(), "render", blend_file_name)
    else:
        blend_file_path = blend_file_name

    output_path = json_data["output_path"]

    if os.sep not in output_path:
        output_path = os.path.join(os.getcwd(), "output", "output_image")
    else:
        output_path = output_path

    if blender_path:
        print("Blender path is None please run set_blender() function.")
        exit()

    image_render_command = [blender_path, "-b", blend_file_path, "-o" , output_path, "-P", "/content/settings/image_settings.py"]
    animation_render_command = [blender_path, "-b", blend_file_path, "-o" , output_path, "-P", "/content/settings/animation_settings.py", "-a"]

    if render_animation:
        run_command(animation_render_command)
    else:
        run_command(image_render_command)