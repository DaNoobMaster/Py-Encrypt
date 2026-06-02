import streamlit as st
from cryptography.fernet import Fernet
import base64
import hashlib

st.set_page_config(page_title="🔐 Encryption Tool", layout="wide")
st.title("🔐 File Encryption Tool")

# Initialize session state
if 'fernet' not in st.session_state:
    st.session_state.fernet = None
if 'current_key' not in st.session_state:
    st.session_state.current_key = None

def convert_key(input_key):
    """Convert a password/string into a valid Fernet key"""
    try:
        decoded = base64.urlsafe_b64decode(input_key.encode())
        if len(decoded) == 32:
            return input_key.encode()
        if input_key == "":
            return ""
    except Exception:
        pass
    
    # Convert normal password/string into Fernet key
    hashed_key = hashlib.sha256(input_key.encode()).digest()
    return base64.urlsafe_b64encode(hashed_key)

def update_fernet():
    """Update the fernet object with the current key"""
    if st.session_state.key_input:
        new_key = convert_key(st.session_state.key_input)
        st.session_state.current_key = new_key
        st.session_state.fernet = Fernet(new_key)

# Sidebar for key management
st.sidebar.header("🔑 Key Management")

col1, col2 = st.sidebar.columns(2)
if col1.button("Generate New Key"):
    new_key = Fernet.generate_key()
    st.session_state.key_input = new_key.decode()
    update_fernet()
    st.rerun()

if col2.button("Clear Key"):
    st.session_state.key_input = ""
    st.session_state.fernet = None
    st.session_state.current_key = None
    st.rerun()

# Key input
key_input = st.sidebar.text_area(
    "Enter or paste your encryption key:",
    value=st.session_state.get('key_input', ''),
    key='key_input',
    on_change=update_fernet,
    height=100
)

if st.session_state.fernet:
    st.sidebar.success("✓ Key loaded successfully")
else:
    st.sidebar.warning("⚠️ No valid key loaded")

# Main content
st.divider()
tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
    st.header("Encrypt a File")
    
    if not st.session_state.fernet:
        st.error("Please load a key first using the sidebar")
    else:
        uploaded_file = st.file_uploader("Choose a file to encrypt", key="encrypt_file")
        
        if uploaded_file:
            if st.button("🔒 Encrypt File"):
                try:
                    file_data = uploaded_file.read()
                    encrypted_data = st.session_state.fernet.encrypt(file_data)
                    
                    # Create download button
                    st.download_button(
                        label="Download Encrypted File",
                        data=encrypted_data,
                        file_name=f"{uploaded_file.name}.encrypted",
                        mime="application/octet-stream"
                    )
                    st.success("✓ File encrypted successfully!")
                except Exception as e:
                    st.error(f"Error encrypting file: {str(e)}")

with tab2:
    st.header("Decrypt a File")
    
    if not st.session_state.fernet:
        st.error("Please load a key first using the sidebar")
    else:
        uploaded_file = st.file_uploader("Choose a file to decrypt", key="decrypt_file")
        
        if uploaded_file:
            if st.button("🔓 Decrypt File"):
                try:
                    encrypted_data = uploaded_file.read()
                    decrypted_data = st.session_state.fernet.decrypt(encrypted_data)
                    
                    # Create download button
                    st.download_button(
                        label="Download Decrypted File",
                        data=decrypted_data,
                        file_name=uploaded_file.name.replace(".encrypted", ""),
                        mime="application/octet-stream"
                    )
                    st.success("✓ File decrypted successfully!")
                except Exception as e:
                    st.error(f"Error decrypting file: {str(e)}")

st.divider()
st.markdown("""
### How to use:
1. **Generate a Key** or paste an existing key in the sidebar
2. **Upload a file** to encrypt or decrypt
3. **Click the button** to process the file
4. **Download** the result

### Key Tips:
- Save your key somewhere safe!
- Use the same key to decrypt files you encrypted
- Remember: Without the key, encrypted files cannot be recovered
""")
