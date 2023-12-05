st.title("Line Plot Example")
data = pd.DataFrame({
    "x": [1, 2, 3, 4],                # Load sample data
    "y": [10, 20, 30, 40]})
plt.plot(data["x"], data["y"])         # Plot the data
st.pyplot()                            # Show the plot in the Streamlit app
