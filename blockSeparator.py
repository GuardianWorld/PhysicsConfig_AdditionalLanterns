import os

input_folder = "C:/Users/drxmi/Desktop/AdditionalLanterns-fabric-1.20/src/generated/resources/assets/additionallanterns/models/block"  # Replace with the path to your folder containing the JSON files

chain_names = []
lantern_names = []

for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        name = filename[:-5]  # Remove the .json extension

        if "off" in name or "hanging" in name:
            continue  # Skip filenames with "off" or "hanging"

        if "chain" in name:
            chain_names.append(name)
        elif "lantern" in name:
            lantern_names.append(name)

# Save chain names to a file
with open("chain_names.txt", "w") as chain_file:
    for name in chain_names:
        chain_file.write("additionallanterns:" + name + "\n")

# Save lantern names to a file
with open("lantern_names.txt", "w") as lantern_file:
    for name in lantern_names:
        lantern_file.write("additionallanterns:" + name + "\n")

print("Names have been extracted and saved to chain_names.txt and lantern_names.txt")