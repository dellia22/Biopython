
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
#get_ipython().magic(u'pylab inline')


# # Load rhodopsin metadata

# In[3]:


rhod_df = pd.read_csv("./rhodopsin_metadata.csv")
print(rhod_df)


# # Load blastp results
# 
# To generate the blastp results the following command was used:
# 
# `blastp -evalue 0.001 -query rhodopsins.fasta -subject rhodopsins.fasta -out rhodopsins.out  -outfmt 6`

# In[4]:


blast_columns = 'protein proteinB pident length mismatch gapopen qstart qend sstart send evalue bitscore'.split(" ")


# In[5]:


df  = pd.read_csv("./rhodopsins.out", sep="\t", names=blast_columns)


# In[6]:


len(df)


# In[7]:


#df = df.drop_duplicates(["protein", "proteinB"])


# In[8]:


#df["members"] = df.apply(lambda row: str(sorted([row['protein'], row['proteinB']])), axis=1)


# In[9]:


#df = df.sort_values(by=["members", "length"], ascending=False)


# In[10]:


#df = df.drop_duplicates("members")


# In[11]:


#df.describe()


# In[12]:


#df.loc[(df["protein"] == "NR")]


# ## Create column color dataframe

# In[13]:


#lut = dict(zip(['Type-1','Heliorhodopsin'], ['gray', '#7137c8']))


# In[14]:


#col_colors = pd.concat([rhod_df["rhodopsin"],           rhod_df["Rhodopsin type"].map(lut)], axis=1)


# In[15]:


# In[16]:


#col_colors.rename(columns={"rhodopsin":"protein"}, inplace=True)


# In[17]:


# In[51]:


#col_colors.set_index("protein", inplace=True)
#print(col_colors)

# In[61]:


# ## Create subset blast results df

# In[19]:


id_df = df[["protein", "proteinB", "pident", "bitscore", "length"]]


# In[20]:


# In[21]:


id_df2 = id_df[id_df.columns[[1,0,2,3,4]]]


# In[22]:


id_df2.rename(columns={"protein":"proteinB", "proteinB":"protein"}, inplace=True)


# In[23]:


id_df = pd.concat([id_df, id_df2])


# In[24]:


id_df = id_df.drop_duplicates(["protein", "proteinB"])


# In[25]:


# ## Create pairwise matrix from blastp results using pident

# In[26]:


# We filter alignments of at least 90% the length of the shortest rhodopsin in the dataset.
id_df_filtered = id_df.loc[id_df["length"] > 200]


# In[27]:


id_df_filtered = id_df_filtered.pivot(index="protein", columns="proteinB", values="pident")
id_df_filtered.fillna(0, inplace=True)


# In[30]:



# In[31]:


#This affects the amount of labels to display in the rows/columns from the heatmap
plot_size = (20,20)


# In[29]:


g = sns.clustermap(id_df_filtered, figsize=plot_size,                   robust=False, annot=False)


# In[33]:


#g = sns.clustermap(id_df_filtered, col_colors=col_colors, figsize=plot_size,                   robust=False, annot=False)


# Create legend for dendrogram
#for label in rhod_df["Rhodopsin type"].unique():
 #   g.ax_row_dendrogram.bar(0, 0, color=lut[label],
                   #         label=label, linewidth=0)

#l2 = g.ax_row_dendrogram.legend(loc='upper center', ncol=1, fontsize=10);
#l2.set_title(title="Rhodopsin type", prop={'size':10})
#g.ax_row_dendrogram.set_ylim([0,0]); # Hide right dendrogram but keep legend

#set the position of the colorbar[x,]
#g.ax_heatmap.collections[0].colorbar.set_label("% Identity", size=18)
#g.ax_heatmap.collections[0].colorbar.ax.tick_params(labelsize=16) 
#g.cax.set_position([.135,.18,.02,.45])


# In[70]:


from PIL import Image
from io import BytesIO
# save figure
# (1) save the image in memory in PNG format
png1 = BytesIO()
g.savefig(png1, format='png', dpi=300)

# (2) load this image into PIL
png2 = Image.open(png1)

# (3) save as TIFF
png2.save('blastp_clustermap_uncompressed.tiff')
png1.close()
png2.close()


# In[ ]:


# compress the tiff file
# install libtiff for the compression of the tiff file
#get_ipython().system(u'tiffcp -c lzw blastp_clustermap_uncompressed.tiff blastp_clustermap.tiff')


# In[ ]:


#get_ipython().system(u'rm blastp_clustermap_uncompressed.tiff')

