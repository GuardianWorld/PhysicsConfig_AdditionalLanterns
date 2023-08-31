import json

static_layout_chain = {
    "blockID": "minecraft:chain",
    "settingID": 0,
    "Linked Physics": True,
    "Fixed on bottom": False,
    "No gravity": False,
    "Side connection": True,
    "Hitbox scale x": 1.5,
    "Hitbox scale y": 1.0,
    "Hitbox scale z": 1.5,
    "Stiffness": 60.0,
    "Damping": 40.0
}

static_layout_lantern = {
    "blockID": "minecraft:soul_lantern",
    "settingID": 0,
    "Linked Physics": True,
    "Can link": "minecraft:chain",
    "Fixed on bottom": False,
    "No gravity": False,
    "Side connection": False,
    "Hitbox scale x": 1.0,
    "Hitbox scale y": 1.0,
    "Hitbox scale z": 1.0,
    "Stiffness": 5000.0,
    "Damping": 100.0
}

input_file_path_chain = "chain_names.txt"  # Replace with your input file path
input_file_path_lantern = "lantern_names.txt"  # Replace with your input file path
output_file_path = "output_layouts.txt"  # Replace with your desired output file path

# Create a dictionary to map lantern materials to chain names
lantern_to_chain_mapping = {
    "amethyst": "amethyst_chain",
    "andesite": "andesite_chain",
    "basalt": "basalt_chain",
    "blackstone": "blackstone_chain",
    "bone": "bone_chain",
    "bricks": "bricks_chain",
    "cobbled_deepslate": "cobbled_deepslate_chain",
    "cobblestone": "cobblestone_chain",
    "copper": "copper_chain",
    "crimson": "crimson_chain",
    "dark_prismarine": "dark_prismarine_chain",
    "deepslate_bricks": "deepslate_bricks_chain",
    "diamond": "diamond_chain",
    "diorite": "diorite_chain",
    "emerald": "emerald_chain",
    "end_stone": "end_stone_chain",
    "exposed_copper": "exposed_copper_chain",
    "gold": "gold_chain",
    "granite": "granite_chain",
    "mossy_cobblestone": "mossy_cobblestone_chain",
    "netherite": "netherite_chain",
    "normal": "normal_chain",
    "normal_nether_bricks": "normal_nether_bricks_chain",
    "normal_sandstone": "normal_sandstone_chain",
    "obsidian": "obsidian_chain",
    "oxidized_copper": "oxidized_copper_chain",
    "prismarine": "prismarine_chain",
    "purpur": "purpur_chain",
    "quartz": "quartz_chain",
    "red_nether_bricks": "red_nether_bricks_chain",
    "red_sandstone": "red_sandstone_chain",
    "smooth_stone": "smooth_stone_chain",
    "stone_bricks": "stone_bricks_chain",
    "stone": "stone_chain",
    "warped": "warped_chain",
    "waxed_copper": "waxed_copper_chain",
    "waxed_exposed_copper": "waxed_exposed_copper_chain",
    "waxed_oxidized_copper": "waxed_oxidized_copper_chain",
    "waxed_weathered_copper": "waxed_weathered_copper_chain",
    "weathered_copper": "weathered_copper_chain",
}

lantern_groups = {}

colors = [
    "black", "blue", "brown", "cyan", "gray", "green", "light_blue",
    "light_gray", "lime", "magenta", "orange", "pink", "purple",
    "red", "white", "yellow"
]

for material, chain in lantern_to_chain_mapping.items():
    lanterns = []
    for color in colors:
        lantern_variant = f"additionallanterns:{color}_{material}_lantern"
        lanterns.append(lantern_variant)
    lanterns.append(f"additionallanterns:{material}_lantern")
    lantern_groups[material] = lanterns

output_file_path = "output_layouts.txt"  # Replace with your desired output file path

modified_layouts = []

for material, lanterns in lantern_groups.items():
    chain_name = lantern_to_chain_mapping[material]  # Get the chain name for this material
    
    # Create the chain layout for this material
    chain_layout = static_layout_chain.copy()
    chain_layout["blockID"] = f"additionallanterns:{chain_name}"
    modified_layouts.append(chain_layout)

    for lantern_name in lanterns:
        lantern_layout = static_layout_lantern.copy()
        lantern_layout["blockID"] = f"{lantern_name}"
        modified_layouts.append(lantern_layout)
        
        # Create layouts for all possible combinations of lanterns and chains
        for other_material, other_lanterns in lantern_groups.items():
            other_chain_name = lantern_to_chain_mapping[other_material]
            lantern_layout_combination = static_layout_lantern.copy()
            lantern_layout_combination["blockID"] = f"{lantern_name}"
            lantern_layout_combination["Can link"] = f"additionallanterns:{other_chain_name}"
            modified_layouts.append(lantern_layout_combination)

with open(output_file_path, "w") as output_file:
    for layout in modified_layouts:
        output_file.write("\t{\n")
        for index, (key, value) in enumerate(layout.items()):
            if isinstance(value, bool):
                value = str(value).lower()

            output_file.write(f'    \t"{key}": {json.dumps(value)}')

            if index != len(layout) - 1:
                output_file.write(",")

            output_file.write("\n")

        output_file.write("\t},\n")

print("Layouts have been modified and saved to", output_file_path)