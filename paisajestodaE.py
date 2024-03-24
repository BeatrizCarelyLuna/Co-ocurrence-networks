import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import colors

#corrido el 13 de junio de 2023
#corrido el 27 de junio de 2023
#corrido el 13 de julio de 2023
#corrido el 30 de Octubre de 2023
#corrido y modificado el 5 de marzo de 2024
#redes reales

#parametros que se necesitan para la red
archivo_vertices="Vertices_especies_paisajes.xlsx"
hoja_vertices='verticesR4'
archivo_red="RedesNuevas.xlsx"
#parametros para nombre de la figura
hoja_red='Paisaje4'
fecha='marzo6'
# Se lee los vertices y las aristas de la red
archivo=pd.read_excel(archivo_vertices, sheet_name=hoja_vertices)
archivo2=pd.read_excel(archivo_red, sheet_name=hoja_red)
# Vertices y atributos 
nombre_nodo=archivo['nombre'].values.tolist()
clave_nodo=archivo['clave'].values.tolist()
labels=dict(zip(clave_nodo,nombre_nodo))
tama_nodo=archivo['IAR'].values.tolist()
tama_nodo_big=list(np.array(tama_nodo)*250)

#Aristas y atributos
# In es el que pasa
entrada=archivo2['In'].values.tolist()
#Out el que lo sigue
salida=archivo2['Out'].values.tolist()
edge_colors=archivo2['Day'].values.tolist()
pvalue=archivo2['pvalround'].values.tolist()
pesoArista=archivo2['freq2'].values.tolist()

#Construccion de la red
RedMami=nx.DiGraph()
RedMami.add_nodes_from(clave_nodo)
for k in range(0,len(salida),1):
    RedMami.add_edge(salida[k],entrada[k],pesoA=pesoArista[k],Color_Aristas=edge_colors[k],pval=pvalue[k])

#SE DIBIJA LA RED  

fig = plt.figure()
#Posicion de los vertices
pos2 ={1: np.array([-0.10691077,  -0.45332362]), 2: np.array([-0.25691077, 0.23716172]), 3: np.array([0.20691077, -0.95332362]), 4: np.array([-0.51404956, 0.23716172]), 5: np.array([-0.20691077,  -0.95332362]), 6: np.array([-0.49404956, 0.95332362]), 7: np.array([0.4691077,  -0.8332362]), 8: np.array([-0.51404956,  -0.45332362]), 9: np.array([-0.19404956, 0.95332362]), 10: np.array([0.390691077,  -0.480332362]), 11: np.array([0.45404956, 0.23716172]), 12: np.array([-0.51404956,  -0.95332362]), 13: np.array([0.49404956, 0.95332362]), 14: np.array([0.09404956, 0.23716172])}
color_arista=nx.get_edge_attributes(RedMami,'Color_Aristas')
C_arista=[color_arista.get(edge) for edge in RedMami.edges()]
nodes = nx.draw_networkx_nodes(RedMami, pos2, node_size=tama_nodo_big, node_color='blue',alpha=0.2)
edges = nx.draw_networkx_edges(RedMami, pos2, node_size=tama_nodo_big, arrowstyle='->', arrowsize=40,connectionstyle='arc3, rad=0.2', width=6,edge_color=C_arista,edge_cmap=plt.cm.cividis)
for ele in pos2:
   pos2[ele]=pos2[ele]-[0,-0.02]

nx.draw_networkx_labels(RedMami,pos2,labels,font_size=13,font_weight='bold')
pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.cividis)
pc.set_array([0,4,8,12,16,20])
plt.colorbar(pc, cax=None, ax=None)
ax = plt.gca()
ax.set_axis_off()
#plt.show()
fig = mpl.pyplot.gcf()
fig.set_size_inches(14, 9)
#Se guarda la red
plt.savefig(hoja_red+fecha+'N.png',bbox_inches='tight',pad_inches=2,dpi=300)
plt.close()
