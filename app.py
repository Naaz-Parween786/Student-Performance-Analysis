import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data ---
df = pd.read_csv("data/student_performance.csv")

# --- Page Title ---
st.title("Student Performance Analysis")
st.write("Exploratory data analysis of 1,000 student records.")

# --- Show Raw Data ---
st.subheader("Raw Dataset")
st.dataframe(df.head(10))

# --- Score Distribution ---
st.subheader("Score Distribution")
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
sns.histplot(df["math score"], kde=True, ax=axes[0], color="skyblue")
axes[0].set_title("Math Score")
sns.histplot(df["reading score"], kde=True, ax=axes[1], color="orange")
axes[1].set_title("Reading Score")
sns.histplot(df["writing score"], kde=True, ax=axes[2], color="green")
axes[2].set_title("Writing Score")
st.pyplot(fig)

# --- Test Preparation Course ---
st.subheader("Impact of Test Preparation Course")
prep = df.groupby("test preparation course")[
    ["math score", "reading score", "writing score"]
].mean()
fig3, ax3 = plt.subplots(figsize=(8, 5))
prep.plot(kind="bar", ax=ax3, rot=0)
ax3.set_ylabel("Average Score")
ax3.set_xlabel("Test Preparation Course")
ax3.set_title("Impact of Test Preparation Course on Scores")
ax3.set_ylim(0, 100)
st.pyplot(fig3)

# --- Gender Comparison ---
st.subheader("Average Scores by Gender")
gender = df.groupby("gender")[
    ["math score", "reading score", "writing score"]
].mean()
fig6, ax6 = plt.subplots(figsize=(8, 5))
gender.plot(kind="bar", ax=ax6, rot=0)
ax6.set_ylabel("Average Score")
ax6.set_xlabel("Gender")
ax6.set_title("Average Scores by Gender")
ax6.set_ylim(0, 100)
st.pyplot(fig6)

# --- Parental Education ---
st.subheader("Average Scores by Parental Level of Education")
parent = df.groupby("parental level of education")[
    ["math score", "reading score", "writing score"]
].mean()
fig4, ax4 = plt.subplots(figsize=(10, 5))
parent.plot(kind="bar", ax=ax4, rot=45)
ax4.set_ylabel("Average Score")
ax4.set_xlabel("Parental Level of Education")
ax4.set_title("Average Scores by Parental Education")
ax4.set_ylim(0, 100)
plt.tight_layout()
st.pyplot(fig4)

# --- Lunch Type ---
st.subheader("Impact of Lunch Type on Performance")
lunch = df.groupby("lunch")[
    ["math score", "reading score", "writing score"]
].mean()
fig5, ax5 = plt.subplots(figsize=(8, 5))
lunch.plot(kind="bar", ax=ax5, rot=0)
ax5.set_ylabel("Average Score")
ax5.set_xlabel("Lunch Type")
ax5.set_title("Impact of Lunch Type on Scores")
ax5.set_ylim(0, 100)
st.pyplot(fig5)

# --- Correlation Heatmap ---
st.subheader("Correlation Between Subject Scores")
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.heatmap(
    df[["math score", "reading score", "writing score"]].corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax2
)
plt.tight_layout()
st.pyplot(fig2)