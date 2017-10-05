import numpy
from numpy.linalg import svd
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open('../Data/iceice.png')

img_ary = numpy.array(img) / 255

origin_bytes = img_ary.nbytes
print(origin_bytes)
print(img_ary.shape)

img_red = img_ary[:, :, 0]
img_green = img_ary[:, :, 1]
img_blue = img_ary[:, :, 2]
print(img_red.shape)

u_r, s_r, v_r = svd(img_red, full_matrices=True)
u_g, s_g, v_g = svd(img_green, full_matrices=True)
u_b, s_b, v_b = svd(img_blue, full_matrices=True)
print(u_r.shape)

k = 100

u_r_k = u_r[:, 0:k]
v_r_k = v_r[0:k, :]
u_g_k = u_g[:, 0:k]
v_g_k = v_g[0:k, :]
u_b_k = u_b[:, 0:k]
v_b_k = v_b[0:k, :]
s_r_k = s_r[0:k]
s_g_k = s_g[0:k]
s_b_k = s_b[0:k]

compressed_bytes = sum([matrix.nbytes for matrix in [u_r_k, v_r_k, s_r_k, u_g_k, v_g_k, s_g_k, u_b_k, v_b_k, s_b_k]])
print(compressed_bytes)

img_red_appro=numpy.dot(u_r_k,numpy.dot(numpy.diag(s_r_k),v_r_k))
img_green_appro=numpy.dot(u_g_k,numpy.dot(numpy.diag(s_g_k),v_g_k))
img_blue_appro=numpy.dot(u_b_k,numpy.dot(numpy.diag(s_b_k),v_b_k))

row,col,_=img_ary.shape
print(type(col))
image_re=numpy.zeros((row,col,3))
image_re[:,:,0]=img_red_appro
image_re[:,:,1]=img_green_appro
image_re[:,:,2]=img_blue_appro
fig=plt.figure(figsize=(10,5))
a=fig.add_subplot(1,1,1)
implot=plt.imshow(image_re)
plt.show()