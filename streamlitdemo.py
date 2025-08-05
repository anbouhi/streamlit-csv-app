import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 نمایش فایل CSV و نمودار ساده")

# بارگذاری فایل CSV از کاربر
uploaded_file = st.file_uploader("لطفاً فایل CSV خود را انتخاب کنید", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=';')  # اینجا sep=';' اضافه شد
    st.dataframe(df)

    # نمایش جدول داده‌ها
    st.subheader("🔍 پیش‌نمایش داده‌ها")
    st.dataframe(df)

    # گرفتن ستون‌های عددی
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if numeric_cols:
        # انتخاب ستون برای نمودار
        col = st.selectbox("ستونی برای نمودار انتخاب کن", numeric_cols)

        st.subheader(f"📈 نمودار ستونی برای ستون: {col}")
        fig, ax = plt.subplots()
        df[col].value_counts().sort_index().plot(kind='bar', ax=ax)
        st.pyplot(fig)
    else:
        st.warning("هیچ ستونی با نوع عددی پیدا نشد.")
else:
    st.info("👈 لطفاً یک فایل CSV آپلود کنید.")

