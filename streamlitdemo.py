import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 نمودار میله‌ای با دو ستون انتخابی")

uploaded_file = st.file_uploader("لطفاً فایل CSV خود را انتخاب کنید", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';')
    st.subheader("🔍 پیش‌نمایش داده‌ها")
    st.dataframe(df)

    # انتخاب ستون‌های دسته‌ای و عددی
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if categorical_cols and numeric_cols:
        cat_col = st.selectbox("ستون دسته‌ای برای محور X انتخاب کن", categorical_cols)
        num_col = st.selectbox("ستون عددی برای محور Y انتخاب کن", numeric_cols)

        # محاسبه مجموع هر دسته
        grouped = df.groupby(cat_col)[num_col].sum().sort_values(ascending=False)

        st.subheader(f"📈 نمودار میله‌ای مجموع {num_col} بر اساس {cat_col}")
        fig, ax = plt.subplots(figsize=(10, 5))
        grouped.plot(kind='bar', ax=ax)
        ax.set_xlabel(cat_col)
        ax.set_ylabel(f"مجموع {num_col}")
        st.pyplot(fig)

    else:
        st.warning("لطفاً داده‌هایی داشته باشید که حداقل یک ستون دسته‌ای و یک ستون عددی داشته باشند.")
else:
    st.info("👈 لطفاً یک فایل CSV آپلود کنید.")
