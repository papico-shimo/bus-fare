
import streamlit as st
import pandas as pd

df = pd.read_csv("bus_data.csv")
df.columns = df.columns.str.strip()

st.write("列名一覧:", df.columns.tolist())

st.title("バス代自動集計アプリ")

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("アップロードされたデータ")
    st.dataframe(df)

    df["加算するか"] = df["加算するか"].fillna("×")
    df["迎えか"] = df["迎えか"].fillna("×")
    df["遊びか"] = df["遊びか"].fillna("×")
    df["実際のバス代金"] = pd.to_numeric(df["実際のバス代金"], errors="coerce").fillna(0)

    加算数 = (df["加算するか"] == "◯").sum()
    加算計 = 加算数 * 290

    実際合計 = df["実際のバス代金"].sum()
    通学合計 = df[(df["加算するか"] == "◯") & (df["迎えか"] == "×") & (df["遊びか"] == "×")]["実際のバス代金"].sum()
    遊び合計 = df[df["遊びか"] == "◯"]["実際のバス代金"].sum()

    st.subheader("集計結果")
    st.markdown(f"- 実際のバス代金合計: ¥{実際合計:,.0f}")
    st.markdown(f"- 加算回数: {加算数}回 → ¥{加算計:,}")
    st.markdown(f"- 通学等（迎え・遊び以外）合計: ¥{通学合計:,.0f}")
    st.markdown(f"- 遊びの合計: ¥{遊び合計:,.0f}")
