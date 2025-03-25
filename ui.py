import streamlit as st

def get_character_inputs():
    st.subheader("Character Details")

    name = st.text_input("Character Name:")

    # 🧝 Race options with emojis
    race_options = {
        "Aasimar": "✨ Aasimar",
        "Dragonborn": "🐉 Dragonborn",
        "Dwarf": "🛡️ Dwarf",
        "Elf": "🧝 Elf",
        "Firbolg": "🌿 Firbolg",
        "Genasi": "🌀 Genasi",
        "Gnome": "🦉 Gnome",
        "Goblin": "🧠 Goblin",
        "Goliath": "🪓 Goliath",
        "Halfling": "🦶 Halfling",
        "Half-Elf": "🧬 Half-Elf",
        "Human": "🧍 Human",
        "Kenku": "🪶 Kenku",
        "Lizardfolk": "🐍 Lizardfolk",
        "Orc": "🎲 Orc",
        "Tabaxi": "🐾 Tabaxi",
        "Tiefling": "🎭 Tiefling",
        "Triton": "🌊 Triton"
    }

    # 🛡️ Class options with emojis
    class_options = {
        "Barbarian": "🪓 Barbarian",
        "Bard": "🎵 Bard",
        "Cleric": "🙏 Cleric",
        "Druid": "🌿 Druid",
        "Fighter": "⚔️ Fighter",
        "Monk": "🧘 Monk",
        "Paladin": "🛡️ Paladin",
        "Ranger": "🏹 Ranger",
        "Rogue": "🗡️ Rogue",
        "Sorcerer": "🔮 Sorcerer",
        "Warlock": "📜 Warlock",
        "Wizard": "📘 Wizard",
        "Artificer": "🧪 Artificer",
        "Blood Hunter": "🩸 Blood Hunter"
    }

    # 🌀 Subclass options with emojis
    subclass_options = {
        "Champion": "🏆 Champion",
        "Arcane Trickster": "🎯 Arcane Trickster",
        "Life Domain": "💖 Life Domain",
        "Circle of the Moon": "🌕 Circle of the Moon",
        "Oath of Vengeance": "⚖️ Oath of Vengeance",
        "College of Lore": "📚 College of Lore",
        "Hexblade": "🪓 Hexblade",
        "Evocation": "🔥 Evocation",
        "Wild Magic": "🎲 Wild Magic",
        "Battlemaster": "🧠 Battlemaster",
        "Way of Shadow": "🌑 Way of Shadow",
        "Artillerist": "💣 Artillerist"
    }

    # 🧭 Background options with emojis
    background_options = {
        "Acolyte": "🕯️ Acolyte",
        "Charlatan": "🎭 Charlatan",
        "Criminal": "🕵️ Criminal",
        "Entertainer": "🎤 Entertainer",
        "Folk Hero": "🧑‍🌾 Folk Hero",
        "Guild Artisan": "🔧 Guild Artisan",
        "Hermit": "🛖 Hermit",
        "Noble": "👑 Noble",
        "Outlander": "🏞️ Outlander",
        "Sage": "📖 Sage",
        "Sailor": "⚓ Sailor",
        "Soldier": "🎖️ Soldier",
        "Urchin": "🪙 Urchin"
    }

    # Helper for dropdowns
    def emoji_select(label, options_dict):
        display = list(options_dict.values())
        keys = list(options_dict.keys())
        selected_display = st.selectbox(label, display)
        return keys[display.index(selected_display)]

    race = emoji_select("Choose Your Race:", race_options)
    char_class = emoji_select("Choose Your Class:", class_options)
    subclass = emoji_select("Choose Your Subclass:", subclass_options)
    background = emoji_select("Choose Your Background:", background_options)

    personality = st.text_input("Personality:")
    physical_characteristics = st.text_area("Physical Characteristics:")

    return {
        "name": name,
        "race": race,
        "char_class": char_class,
        "subclass": subclass,
        "background": background,
        "personality": personality,
        "physical_characteristics": physical_characteristics
    }
