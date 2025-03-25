def generate_prompt(data):
    name = data["name"]
    race = data["race"]
    char_class = data["char_class"]
    subclass = data["subclass"]
    background = data["background"]
    personality = data["personality"]
    physical_characteristics = data["physical_characteristics"]

    return f"""
    [your long prompt here, including the examples]
    
    Now, generate a new character using the following input:
    **Name:** {name}
    **Race:** {race}
    **Class:** {char_class}
    **Subclass:** {subclass}
    **Background:** {background}
    **Personality:** {personality}
    **Physical Characteristics:** {physical_characteristics}
    
    **Provide:**
    - A deep and compelling backstory
    - Three engaging story hooks
    - An Adobe Firefly image generation prompt
    ---
    """
