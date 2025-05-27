import streamlit as st
import pandas as pd

st.title("🚌 バス代集計アプリ")

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()

    st.subheader("📄 アップロードされたデータ")
    st.dataframe(df)

    # 集計処理
    total_actual_fare = df["実際のバス代金"].sum()
    count_plus = df["加算(+/-)"].fillna("").str.contains(r"\+").sum()
    total_plus_290 = 290 * count_plus
    mask_not_pickup_or_play = df["迎え"].isna() & df["遊び"].isna()
    actual_without_extras = df[mask_not_pickup_or_play]["実際のバス代金"].sum()
    play_fare = df[df["遊び"].notna()]["実際のバス代金"].sum()

    st.subheader("📊 集計結果")
    st.markdown(f"- **合計（実際のバス代金）**：{total_actual_fare:.0f}円")
    st.markdown(f"- **290円 × 加算数**：{total_plus_290:.0f}円")
    st.markdown(f"- **迎え・遊び以外のバス代金**：{actual_without_extras:.0f}円")
    st.markdown(f"- **遊びのバス代金**：{play_fare:.0f}円")