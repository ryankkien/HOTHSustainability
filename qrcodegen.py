#!/usr/bin/env python
# coding: utf-8

# In[10]:


import qrcode
import random
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(random.choice(range(1,100)))
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="cyan")
img


# In[ ]:




