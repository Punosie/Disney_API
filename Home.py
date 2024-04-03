import streamlit as st
from db import get_char

st.header('Disney Character Info')

character_name = st.text_input(label='Character Name')
character_name = character_name.title()

if st.button(label='Submit'):    
    character_info = get_char(character_name)
    print(character_name)
    if character_info:
        st.subheader("**Character Information:**")
        
        # Display Image URL at the top
        if character_info[10]:
            st.image(character_info[10], width=200)
        
        # Display Films
        if character_info[1]:
            st.write(f"**Films:**")
            st.write("  - " + "\n  - ".join(character_info[1].split(',')))
        
        # Display Short Films
        if character_info[2]:
            st.write(f"**Short Films:**")
            st.write("  - " + "\n  - ".join(character_info[2].split(',')))
        
        # Display TV Shows
        if character_info[3]:
            st.write(f"**TV Shows:**")
            st.write("  - " + "\n  - ".join(character_info[3].split(',')))
        
        # Display Video Games
        if character_info[4]:
            st.write(f"**Video Games:**")
            st.write("  - " + "\n  - ".join(character_info[4].split(',')))
        
        # Display Park Attractions
        if character_info[5]:
            st.write(f"**Park Attractions:**")
            st.write("  - " + "\n  - ".join(character_info[5].split(',')))
        
        # Display Allies
        if character_info[6]:
            st.write(f"**Allies:**")
            st.write("  - " + "\n  - ".join(character_info[6].split(',')))
        
        # Display Enemies
        if character_info[7]:
            st.write(f"**Enemies:**")
            st.write("  - " + "\n  - ".join(character_info[7].split(',')))
        
        # Display Source URL
        if character_info[8]:
            st.markdown(f"<a href='{character_info[8]}' target='_blank'>Read more</a>", unsafe_allow_html=True)

    else:
        st.write("Character not found.")