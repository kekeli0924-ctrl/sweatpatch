from PIL import Image
import numpy as np
import sys

def remove_white_bg(input_path, output_path, threshold=240):
    print(f"Processing {input_path}...")
    try:
        img = Image.open(input_path).convert("RGBA")
        data = np.array(img)
        
        # RGB values
        r, g, b, a = data.T
        
        # Identify white pixels (all channels > threshold)
        white_areas = (r > threshold) & (g > threshold) & (b > threshold)
        
        # Make them transparent
        data[..., 3][white_areas.T] = 0
        
        # Save
        img = Image.fromarray(data)
        img.save(output_path)
        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    remove_white_bg(
        "/Users/likerun/Desktop/NEUROHYDRO/images/product_layers_v2.jpg", 
        "/Users/likerun/Desktop/NEUROHYDRO/images/product_layers_v2_transparent.png"
    )
