import streamlit as st
import numpy as np
from PIL import Image
import io

st.title("🔐 Image Encryption and Decryption Demo")

st.write("""
This app demonstrates a simple XOR-based encryption and decryption of images.  
The encrypted image appears like noise, while the decryption recovers the original image.
""")

# Upload image
uploaded_file = st.file_uploader("Upload an Image to Encrypt", type=["png", "jpg", "jpeg"])

if uploaded_file:
    original_image = Image.open(uploaded_file).convert("RGB")
    st.subheader("Original Image")
    st.image(original_image, use_column_width=True)

    # Convert to numpy array
    image_np = np.array(original_image)

    # Generate a random key of same shape
    np.random.seed(42)  # Optional: for consistent encryption
    key = np.random.randint(0, 256, image_np.shape, dtype=np.uint8)

    # Encrypt the image using XOR
    encrypted_image = np.bitwise_xor(image_np, key)
    st.subheader("Encrypted Image")
    st.image(encrypted_image, use_column_width=True, caption="Encrypted (appears like noise)")

    # Decrypt the image
    decrypted_image = np.bitwise_xor(encrypted_image, key)
    st.subheader("Decrypted Image")
    st.image(decrypted_image, use_column_width=True, caption="Decrypted (original restored)")

    # Optional: Save images
    if st.button("Download Encrypted Image"):
        encrypted_pil = Image.fromarray(encrypted_image)
        buf = io.BytesIO()
        encrypted_pil.save(buf, format="PNG")
        st.download_button("Click to Download", buf.getvalue(), file_name="encrypted_image.png", mime="image/png")
