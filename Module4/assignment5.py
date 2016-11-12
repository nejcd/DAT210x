import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Look pretty...
matplotlib.style.use('ggplot')

#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = []
colors = []
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here ..
n = 0
while n <= 355:
    img = misc.imread('E:/Dropbox/DAT210x/Module4/Datasets/ALOI/32/32_r'+str(n)+'.png')
    #img = img[::2, ::2]
    X = (img / 255.0).reshape(-1)
    n += 5
    samples.append(X)
    colors.append('r')
    print ('Reading: r32_r{0}.png'.format(n))

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
n = 110
while n <= 220:
    img = misc.imread('E:/Dropbox/DAT210x/Module4/Datasets/ALOI/32i/32_i'+str(n)+'.png')
    #img = img[::2, ::2]
    X = (img / 255.0).reshape(-1)
    n += 10
    samples.append(X)
    colors.append('b')
    print ('Reading: r32_i{0}.png'.format(n))


#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 
df = pd.DataFrame(samples)

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
from sklearn import manifold
K=6
iso = manifold.Isomap(n_neighbors=K, n_components=3)
iso.fit(df)
manifold.Isomap(eigen_solver='auto', max_iter=None, n_components=3, n_neighbors=K,
    neighbors_algorithm='auto', path_method='auto', tol=0)

manifold = iso.transform(df)




#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
T = pd.DataFrame(manifold)
T.columns = ['component1', 'component2', 'component3']
T.plot.scatter(x='component1', y='component2', marker='o', alpha=0.75, c=colors)


#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
fig = plt.figure()
ax = Axes3D(plt.gcf())
ax.set_title('3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(T.component1, T.component2, T.component3, c=colors)

plt.show()

