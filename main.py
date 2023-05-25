import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns

# Charger les données à partir d'un fichier CSV
sales_data = pd.read_csv("https://raw.githubusercontent.com/<username>/<repo>/<branch>/sales_data.csv")

# Afficher les informations générales sur les données
st.write(sales_data.shape)
st.write(sales_data.dtypes)
st.write(sales_data.describe())

# Ajouter un histogramme pour visualiser la distribution des quantités vendues
st.pyplot(sns.histplot(sales_data["QUANTITY"]))

# Ajouter un nuage de points pour visualiser la relation entre les quantités vendues et les remises
st.pyplot(sns.scatterplot(x="QUANTITY", y="DISCOUNT %", data=sales_data))

# Ajouter un filtre pour afficher les données par type de vente
sale_types = sales_data["SALE TYPE"].unique()
selected_sale_type = st.selectbox("Select a sale type", sale_types)
sale_type_data = sales_data[sales_data["SALE TYPE"] == selected_sale_type]
st.write(sale_type_data)

# Ajouter un diagramme en boîte pour visualiser la distribution des remises
st.pyplot(sns.boxplot(x="DISCOUNT %", data=sales_data))
