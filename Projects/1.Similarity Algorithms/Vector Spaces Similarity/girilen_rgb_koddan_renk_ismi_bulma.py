# region Imports

import json 

# endregion

# region Definitions
def kokal (x):
    return x**(1/2)

def usal (x,y):
    return x**y

def vectorSimilarity (A,B):
    
    if len(A) != len(B):
        return -1
    else:
        len_ = len(A)
        total = 0
        for i in range(len_):
            total += usal(B[i] - (A[i]),2)
        distance =  kokal(total)

    max_distance = 0
    for i in range(len_):
        max_distance += usal(100,2)
    
    max_distance = kokal(max_distance)
    return 1 - (distance / max_distance)

def find_most_similar_color(hex_code):
    input_rgb = [int(hex_code[i:i+2], 16) for i in (0, 2, 4)]
    input_normalized = [input_rgb[i] / 2.55 for i in range(3)]  # Normalize to 0-100 scale

    closest_color_name = None
    highest_similarity = -1

    file_path = "C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\Vector Spaces Similarity\\colors.txt"

    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.strip().strip(',')
            if clean_line:
                code, name = json.loads(clean_line)
                color_rgb = [int(code[i:i+2], 16) for i in (0, 2, 4)]
                color_normalized = [color_rgb[i] / 2.55 for i in range(3)]  # Normalize to 0-100 scale

                similarity = vectorSimilarity(input_normalized, color_normalized)

                if similarity > highest_similarity:
                    highest_similarity = similarity
                    closest_color_name = name

    return closest_color_name


def rgb_to_hexCode(x, y, z):
    return "#{:02X}{:02X}{:02X}".format(x, y, z)

def hex_to_colorName(hex_code):

    color_map = {}
    file_path = "C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\Vector Spaces Similarity\\colors.txt"

    with open(file_path, "r") as file:
        for line in file:
                clean_line = line.strip().strip(',')
                if clean_line:
                    code, name = json.loads(clean_line)
                    color_map[code] = name

    lookup_key = hex_code.lstrip('#')
    
    if color_map.get(lookup_key) is not None:
        return color_map[lookup_key]
    else:
        return find_most_similar_color(lookup_key)

# endregion

print("rgb renk kodu gir:")
r_input = input("R: ")
g_input = input("G: ")
b_input = input("B: ")

hex_code = rgb_to_hexCode(int(r_input), int(g_input), int(b_input))
color_name = hex_to_colorName(hex_code)

print("Hex Kodu:", hex_code)
print("Renk İsmi:", color_name)

