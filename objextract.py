# objextract.py
# Extracts vertex coordinates from an .obj file into RAW_OBJ_VERTS = """..."""

def extract_obj_vertices(input_path, output_path):
    """
    Extracts only vertex coordinates (lines starting with 'v ')
    from a .obj file and writes them into a Python file as:
        RAW_OBJ_VERTS = \"\"\"v x y z ...\"\"\"
    """
    with open(input_path, 'r') as f:
        lines = f.readlines()

    # Keep only lines starting with "v "
    vertex_lines = [line.strip() for line in lines if line.startswith("v ")]

    # Join them into a triple-quoted string
    output_text = 'RAW_OBJ_VERTS = """\n' + "\n".join(vertex_lines) + '\n"""'

    # Write to output file
    with open(output_path, 'w') as f:
        f.write(output_text)

    print(f"✅ Extracted {len(vertex_lines)} vertex lines from '{input_path}'")
    print(f"📁 Saved to: {output_path}")


# Example usage:
if __name__ == "__main__":
    extract_obj_vertices("baby.obj", "baby_vertices.py")

